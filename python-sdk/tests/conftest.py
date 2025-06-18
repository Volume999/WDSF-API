from pathlib import Path

from dotenv import load_dotenv


def pytest_configure() -> None:
    test_env_path = f"{Path(__file__).parent}/resources/.test.env"
    assert load_dotenv(dotenv_path=test_env_path)
