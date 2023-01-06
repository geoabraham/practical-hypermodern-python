import click.testing
import pytest

from practical_hypermodern_python import console


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Título mockeado",
        "extract": "Bajada mockeada",
    }
    return mock
