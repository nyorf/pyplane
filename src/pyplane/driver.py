import asyncio
import logging
import warnings

from .client import Client
from .endpoints.projects import Projects

log = logging.getLogger("pyplane.driver")
log.setLevel(logging.INFO)


class BaseDriver:
    def __init__(
            self, 
            schema: str,
            domain: str,
            basepath: str,
            token: str,
            debug: bool, 
            client_cls
            ):
        if debug:
            log.setLevel(logging.DEBUG)
            log.warning(
                "Careful!!\nSetting debug to True, will reveal your password in the log output if you do driver.login()!\nThis is NOT for production!"
            )
        self.client = client_cls(schema, domain, basepath, token, debug)

    @property
    def projects(self):
        return Projects(self.client)


class Driver(BaseDriver):
    def __init__(
            self, 
            schema: str = 'https',
            domain: str = 'api.plane.so',
            basepath: str = 'api/v1',
            token: str = "",
            debug: bool = False, 
            client_cls=Client
            ):
        super().__init__(schema, domain, basepath, token, debug, client_cls)

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(self, *exc_info):
        return self.client.__exit__(*exc_info)
