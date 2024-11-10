from httpx import HTTPError


class InvalidOrMissingParameters(HTTPError):
    """
    Raised when a plane instance returns a
    400 Bad Request: The server cannot or will not process the request due to something that is perceived to be a client error.
    """


class NoAccessTokenProvided(HTTPError):
    """
    Raised when a plane instance returns a
    401 Unauthorized: Although the HTTP standard specifies “unauthorized”, semantically, this response means “unauthenticated”. That is, the client must authenticate itself to get the requested response.
    """


class ResourceNotFound(HTTPError):
    """
    Raised when a plane instance returns a
    404 Resource not found: The server cannot find the requested resource. This means the URL is not recognized.
    """


class ThrottlingError(HTTPError):
    """
    Raised when a plane instance returns a
    429 Throttling Error: The server is processing too many requests at once and is unable to process your request. Retry the request after some time. You can read our rate-limit doc.
    """


class InternalServerError(HTTPError):
    """
    Raised when a plane instance returns a
    500 Internal Server Error: The server has encountered a situation it does not know how to handle.
    """


class BadGateway(HTTPError):
    """
    Raised when a plane instance returns a
    502 Bad Gateway: This error response means that the server got an invalid response while working as a gateway to get a response needed to handle the request.
    """


class ServiceUnavailable(HTTPError):
    """
    Raised when a plane instance returns a
    503 Service Unavailable: The server is not ready to handle the request. Common causes are a server that is down for maintenance or is overloaded.
    """


class GatewayTimeout(HTTPError):
    """
    Raised when a plane instance returns a
    504 Gateway Timeout: This error response is given when the server acts as a gateway and cannot get a timely response.
    """


class UnknownError(HTTPError):
    """
    Raised when a plane instance returns an error that was not thought of. Probably an issue with the server though.
    """


class NoTokenProvided:
    """
    Raised when auth token is not provided
    """
