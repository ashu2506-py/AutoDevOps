from typer.testing import CliRunner

from app.cli import app


runner = CliRunner()


def test_hello():
    result = runner.invoke(
        app,
        ["hello"]
    )

    assert result.exit_code == 0
    assert "AutoDevOps is running!" in result.stdout


def test_validate_valid_config():
    result = runner.invoke(
        app,
        [
            "validate",
            "configs/example.yaml"
        ]
    )

    assert result.exit_code == 0
    assert "Configuration is valid." in result.stdout


def test_validate_invalid_config(tmp_path):

    config = tmp_path / "invalid.yaml"

    config.write_text(
        """
project:
  name: demo

resources: {}
"""
    )

    result = runner.invoke(
        app,
        [
            "validate",
            str(config)
        ]
    )

    assert result.exit_code == 1
    assert "Configuration is invalid" in result.stderr


def test_validate_missing_file():

    result = runner.invoke(
        app,
        [
            "validate",
            "configs/missing.yaml"
        ]
    )

    assert result.exit_code == 1
    assert "ERROR:" in result.stderr


def test_generate():

    result = runner.invoke(
        app,
        [
            "generate",
            "configs/example.yaml"
        ]
    )

    assert result.exit_code == 0
    assert "Terraform generated successfully" in result.stdout
    assert "Ansible generated successfully" in result.stdout
    assert "Kubernetes generated successfully" in result.stdout


def test_plan():

    result = runner.invoke(
        app,
        [
            "plan",
            "configs/example.yaml"
        ]
    )

    assert result.exit_code == 0
    assert "Plan completed in DRY-RUN mode." in result.stdout
    assert "State saved successfully." in result.stdout


def test_deploy():

    result = runner.invoke(
        app,
        [
            "deploy",
            "configs/example.yaml"
        ]
    )

    assert result.exit_code == 0
    assert "Deployment simulation completed safely." in result.stdout
    assert "State saved successfully." in result.stdout


def test_estimate():

    result = runner.invoke(
        app,
        [
            "estimate",
            "configs/example.yaml"
        ]
    )

    assert result.exit_code == 0
    assert "Estimated Monthly Cost" in result.stdout
    assert "Estimated Total" in result.stdout


def test_logs(capsys):

    from app.cli import logs

    logs()

    captured = capsys.readouterr()

    assert "COMMAND:" in captured.out
def test_status():

    result = runner.invoke(
        app,
        ["status"]
    )

    assert result.exit_code == 0
    
def test_estimate_invalid_config(tmp_path):

    config = tmp_path / "invalid.yaml"

    config.write_text(
        """
project:
  name: demo

resources: {}
"""
    )

    result = runner.invoke(
        app,
        [
            "estimate",
            str(config)
        ]
    )

    assert result.exit_code == 1
    assert "Configuration is invalid" in result.stderr


def test_generate_invalid_config(tmp_path):

    config = tmp_path / "invalid.yaml"

    config.write_text(
        """
project:
  name: demo

resources: {}
"""
    )

    result = runner.invoke(
        app,
        [
            "generate",
            str(config)
        ]
    )

    assert result.exit_code == 1
    assert "Configuration is invalid" in result.stderr


def test_plan_invalid_config(tmp_path):

    config = tmp_path / "invalid.yaml"

    config.write_text(
        """
project:
  name: demo

resources: {}
"""
    )

    result = runner.invoke(
        app,
        [
            "plan",
            str(config)
        ]
    )

    assert result.exit_code == 1
    assert "Configuration is invalid" in result.stderr


def test_deploy_invalid_config(tmp_path):

    config = tmp_path / "invalid.yaml"

    config.write_text(
        """
project:
  name: demo

resources: {}
"""
    )

    result = runner.invoke(
        app,
        [
            "deploy",
            str(config)
        ]
    )

    assert result.exit_code == 1
    assert "Configuration is invalid" in result.stderr