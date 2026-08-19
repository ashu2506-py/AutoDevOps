import subprocess
import sys

from app.executor import Executor
from app.logger import DeploymentLogger

def test_dry_run(tmp_path):

    logger = DeploymentLogger(
        tmp_path / "deployment.log"
    )

    executor = Executor(
        logger=logger
    )

    result = executor.run(
        ["terraform", "apply"],
        dry_run=True
    )

    assert result.returncode == 0
    assert result.skipped is True

    assert "DRY-RUN" in result.stdout


def test_missing_command(tmp_path):

    logger = DeploymentLogger(
        tmp_path / "deployment.log"
    )

    executor = Executor(
        logger=logger
    )

    result = executor.run(
        ["this-command-does-not-exist"],
        dry_run=False
    )

    assert result.returncode == 127


def test_log_created(tmp_path):

    log_file = (
        tmp_path /
        "deployment.log"
    )

    logger = DeploymentLogger(
        log_file
    )

    executor = Executor(
        logger=logger
    )

    executor.run(
        ["terraform", "plan"],
        dry_run=True
    )

    assert log_file.exists()

    content = log_file.read_text()

    assert "terraform plan" in content
    
import sys


def test_command_timeout(tmp_path, monkeypatch):

    logger = DeploymentLogger(
        tmp_path / "deployment.log"
    )

    executor = Executor(
        logger=logger
    )

    def fake_run(*args, **kwargs):
        raise subprocess.TimeoutExpired(
            cmd=args[0],
            timeout=kwargs.get("timeout")
        )

    monkeypatch.setattr(
        "app.executor.subprocess.run",
        fake_run
    )

    result = executor.run(
        [
            sys.executable,
            "-c",
            "print('test')"
        ],
        dry_run=False
    )

    assert result.returncode == 124
    assert "timed out" in result.stderr
def test_command_failure(tmp_path):

    logger = DeploymentLogger(
        tmp_path / "deployment.log"
    )

    executor = Executor(
        logger=logger
    )

    result = executor.run(
        [
            sys.executable,
            "-c",
            "import sys; print('error'); sys.exit(2)"
        ],
        dry_run=False
    )

    assert result.returncode == 2
    assert "error" in result.stdout


def test_command_timeout(tmp_path, monkeypatch):

    logger = DeploymentLogger(
        tmp_path / "deployment.log"
    )

    executor = Executor(
        logger=logger
    )

    def fake_run(*args, **kwargs):
        raise subprocess.TimeoutExpired(
            cmd=args[0],
            timeout=kwargs.get("timeout")
        )

    monkeypatch.setattr(
        "app.executor.subprocess.run",
        fake_run
    )

    result = executor.run(
        [
            sys.executable,
            "-c",
            "print('test')"
        ],
        dry_run=False
    )

    assert result.returncode == 124
    assert "timed out" in result.stderr