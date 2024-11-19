import logging
import httpx
from .version import version
from .exceptions import(
    InvalidOrMissingParameters,
    NoAccessTokenProvided,
    ResourceNotFound,
    ThrottlingError,
    InternalServerError,
    BadGateway,
    ServiceUnavailable,
    GatewayTimeout,
    UnknownError,
    NoTokenProvided
)
from .endpoints.projects import Projects

log = logging.getLogger("pyplane.client")
log.setLevel(logging.INFO)


class BaseClient:
    def __init__(
            self, 
            schema: str,
            domain: str,
            basepath: str,
            token: str,
            debug: bool
            ):
        self._schema = schema
        self._domain = domain
        self._basepath = basepath
        if schema == 'https':
            self._port = 443
            self._ssl_verification = True
        elif schema == 'http':
            self._port = 80
            self._ssl_verification = False
        else:
            raise Exception("Unsupported protocol. Only http:// and https:// are supported.")
        if debug:
            self._activate_verbose_logging()
        self._useragent = f'PyPlane/{version}'
        self._token = token
        self._timeout = 30

    @staticmethod
    def _make_url(schema, domain, port, basepath):
        return f"{schema}://{domain}:{port}/{basepath}/"

    @staticmethod
    def _activate_verbose_logging(level=logging.DEBUG):
        log.setLevel(level)
        # enable trace level logging in httpx
        httpx_log = logging.getLogger("httpx")
        httpx_log.setLevel("TRACE")
        httpx_log.propagate = True

    @property
    def request_timeout(self):
        """
        :return: The configured timeout for the requests
        """
        return self._timeout
    
    @property
    def ssl_verification(self):
        """Gets current setting for SSL certificate verification during requests

        Returns:
            ssl_verification (boolean): True/False setting for SSL certificate verification during requests
        """
        return self._ssl_verification
        
    @ssl_verification.setter
    def ssl_verification(self, ssl_verification: bool):
        """Sets a new setting for SSL certificate verification during requests

        Args:
            ssl_verification (bool): True/False setting for SSL certificate verification during requests
        """
        self._ssl_verification = ssl_verification

    @property
    def port(self):
        """Gets port value as class(int)

        Returns:
            port (int): current port for the API endpoint URL
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets a port for the client instance

        Args:
            port (int): port for the API endpoint URL
        """
        self._port = port

    @property
    def url(self):
        """Full URL for the API endpoint. Can't be set manually.

        Returns:
            url (str): a URL used for this client instance
        """
        return self._make_url(self._schema, self._domain, self._port, self._basepath)

    @property
    def token(self):
        """Gets the token for client's current instance. Default: None

        Returns:
            token (str): API token for the Plane workspace ('X-API-KEY')
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets a new token for the client's current instance. Accepts string class only.

        Args:
            token (str): API token for the Plane workspace ('X-API-KEY')
        """
        self._token = token

    @property
    def useragent(self):
        """Gets the useragent that is being passed in the headers of each request. Default: 'PyPlane/<current_version>'

        Returns:
            useragent (str): UA string for requests
        """
        return self._useragent

    @useragent.setter
    def useragent(self, ua: str):
        """Sets a new useragent that is being passed in the headers of each request.

        Args:
            ua (str): UA string for requests
        """
        self._useragent = ua

    @property
    def settings(self):
        settings_str = f"""Your current client settings are:
Schema: {self._schema}
Domain: {self._domain}
Port: {self._port}
Basepath: {self._basepath}
UserAgent: {self._useragent}
Timeout: {self._timeout}
Full URL: {self._make_url(self._schema, self._domain, self._port, self._basepath)}
"""
        """Returns a summary of the client's settings

        Returns:
            settings (str): Client settings
        """
        return settings_str
    
    def headers(self):
        if self._token == "":
            raise NoTokenProvided("It seems that you forgot to specify your auth token.") from None
        else:
            return {
                "Content-Type": "application/json",
                "X-API-KEY": self._token,
                "User-Agent": self._useragent
        }

    def _build_request(self, method, payload=None, params=None, basepath=None):
        if params is None:
            params = {}
        if basepath:
            url = self._make_url(self._schema, self._domain, self._port, basepath)
        else:
            url = self._make_url(self._schema, self._domain, self._port, self._basepath)

        request_params = {"headers": self.headers(), "timeout": self.request_timeout}

        if params is not None:
            request_params["params"] = params

        if method in ("post", "put", "patch"):
            if payload is not None:
                request_params["json"] = payload

        return self._get_request_method(method, self.client), url, request_params
    
    @staticmethod
    def _check_response(response):
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            try:
                data = e.response.json()
                message = data.get("message", data)
            except ValueError:
                log.debug("Could not convert response to json")
                message = response.text
            log.error(message)

            if e.response.status_code == 400:
                raise InvalidOrMissingParameters(message) from None
            elif e.response.status_code == 401:
                raise NoAccessTokenProvided(message) from None
            elif e.response.status_code == 404:
                raise ResourceNotFound(message) from None
            elif e.response.status_code == 429:
                raise ThrottlingError(message) from None
            elif e.response.status_code == 500:
                raise InternalServerError(message) from None
            elif e.response.status_code == 502:
                raise BadGateway(message) from None
            elif e.response.status_code == 503:
                raise ServiceUnavailable(message) from None
            elif e.response.status_code == 504:
                raise GatewayTimeout(message) from None
            else:
                raise UnknownError from None

        log.debug(response)

    @staticmethod
    def _get_request_method(method, client):
        method = method.lower()
        if method == "post":
            return client.post
        elif method == "put":
            return client.put
        elif method == "delete":
            return client.delete
        elif method == "patch":
            return client.patch
        else:
            return client.get


class Client(BaseClient):
    def __init__(
            self, 
            schema: str = 'https',
            domain: str = 'api.plane.so',
            basepath: str = 'api/v1',
            token: str = None,
            debug: bool = False
            ):
        super().__init__(schema, domain, basepath, token, debug)
        self.client = httpx.Client(
            http2=False,
            verify=self._ssl_verification
        )

    def make_request(self, method, endpoint, payload=None, params=None, basepath=None):
        request, url, request_params = self._build_request(method, payload, params, basepath)
        response = request(url + endpoint, **request_params)

        self._check_response(response)
        return response

    @property
    def projects(self):
        return Projects(self)

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(self, *exc_info):
        return self.client.__exit__(*exc_info)

    def get(self, endpoint, payload=None, params=None):
        print([endpoint, payload, params])
        response = self.make_request("get", endpoint, payload=payload, params=params)

        if response.headers["Content-Type"] != "application/json":
            log.debug("Response is not application/json, returning raw response")
            return response

        try:
            return response.json()
        except ValueError:
            log.debug("Could not convert response to json, returning raw response")
            return response

    def post(self, endpoint, payload=None, params=None):
        return self.make_request("post", endpoint, payload=payload, params=params).json()

    def put(self, endpoint, payload=None, params=None, data=None):
        return self.make_request("put", endpoint, payload=payload, params=params).status_code

    def patch(self, endpoint, payload=None, params=None, data=None):
        return self.make_request("patch", endpoint, payload=payload, params=params).status_code

    def delete(self, endpoint, payload=None, params=None, data=None):
        return self.make_request("delete", endpoint, payload=payload, params=params).status_code

