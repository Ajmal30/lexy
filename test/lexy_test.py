from click.testing import CliRunner
from lexy.lexy import lexy


def test_lexy():
    runner = CliRunner()
    result = runner.invoke(lexy, ["python"])
    assert result.exit_code == 0


def test_lexy_with_invalid_language():
    runner = CliRunner()
    result = runner.invoke(lexy, ["invalid_language"])
    assert result.exit_code == 1
    assert "not found" in result.output


def test_lexy_with_modified():
    runner = CliRunner()
    result = runner.invoke(lexy, ["modified"])
    assert result.exit_code == 0
    assert "The last time Lexy was updated is:" in result.output
