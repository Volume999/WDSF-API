from pydantic import HttpUrl, SecretStr

from wdsf_python_sdk.config import (
    load_wdsf_client_config,
    WdsfClientConfig,
    BasicAuthCredentials,
)


def test_load_wdsf_client_config_returns_expected_config():
    # Then
    assert load_wdsf_client_config() == WdsfClientConfig(
        url=HttpUrl("http://some-url.com"),
        auth=BasicAuthCredentials(
            username="some-user", password=SecretStr("some-password")
        ),
    )
