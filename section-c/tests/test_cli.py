"""test isbn validation cli application"""
from typer.testing import CliRunner

from eyesbeen.cli import app

runner = CliRunner()


def test_usage():
    result = runner.invoke(app, [])
    assert result.exit_code != 0


def test_invalid_isbn10():
    result = runner.invoke(app, ["031606652X"])
    assert result.exit_code == 0
    assert "Invalid" in result.stdout


def test_valid_isbn10():
    result = runner.invoke(app, ["9780316066525"])
    assert result.exit_code == 0
    assert "Valid" in result.stdout
