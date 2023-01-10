"""Package-wide test fixtures."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
from _pytest.config import Config


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Título mockeado",
        "extract": "Bajada mockeada",
    }
    return mock


def pytest_configure(config: Config) -> None:
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
