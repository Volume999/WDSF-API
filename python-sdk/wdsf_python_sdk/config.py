import os

from pydantic import BaseModel, HttpUrl, SecretStr


class BasicAuthCredentials(BaseModel):
    username: str
    password: SecretStr


class WdsfClientConfig(BaseModel):
    url: HttpUrl
    auth: BasicAuthCredentials


def load_wdsf_client_config() -> WdsfClientConfig:
    return WdsfClientConfig(
        url=HttpUrl(os.environ["WDSF_URL"]),
        auth=BasicAuthCredentials(
            username=os.environ["WDSF_USER"], password=SecretStr(os.environ["WDSF_PWD"])
        ),
    )
