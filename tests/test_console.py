from unittest.mock import Mock

import click.testing
import pytest
import requests
from pytest_mock import MockFixture
from click.testing import CliRunner

from practical_hypermodern_python import console


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock):
    result = runner.invoke(console.main)
    assert "Título mockeado" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock):
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_es_wikipedia_org(runner: CliRunner, mock_requests_get: Mock):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner: CliRunner, mock_requests_get: Mock):
    mock_requests_get.side_effect = Exception("Crash!")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner: CliRunner, mock_requests_get: Mock):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specified_language(runner: CliRunner, mock_wikipedia_random_page: Mock):
    runner.invoke(console.main, ["--language=de"])
    mock_wikipedia_random_page.assert_called_with(language="de")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner: CliRunner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    return mocker.patch("practical_hypermodern_python.wikipedia.random_page")


@pytest.fixture
def runner() -> CliRunner:
    return click.testing.CliRunner()
