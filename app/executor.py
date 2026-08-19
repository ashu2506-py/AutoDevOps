import shutil
import subprocess
from dataclasses import dataclass

from app.logger import DeploymentLogger


@dataclass
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    skipped: bool = False


class Executor:

    def __init__(self, logger=None):

        self.logger = logger or DeploymentLogger()

    def run(
        self,
        command,
        cwd=None,
        dry_run=True
    ):

        command = list(command)

        command_text = " ".join(command)

        print(f"Command: {command_text}")

        self.logger.write(
            f"COMMAND: {command_text}"
        )

        # -------------------------
        # DRY RUN
        # -------------------------

        if dry_run:

            message = (
                "DRY-RUN: command was not executed."
            )

            print(message)

            self.logger.write(message)

            return CommandResult(
                command=command,
                returncode=0,
                stdout=message,
                stderr="",
                skipped=True
            )

        # -------------------------
        # COMMAND CHECK
        # -------------------------

        if shutil.which(command[0]) is None:

            error = (
                f"Command not found: {command[0]}"
            )

            print(error)

            self.logger.write(
                f"ERROR: {error}"
            )

            return CommandResult(
                command=command,
                returncode=127,
                stdout="",
                stderr=error
            )

        # -------------------------
        # EXECUTE COMMAND
        # -------------------------

        try:

            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=600,
                check=False
            )

            if result.stdout:

                self.logger.write(
                    result.stdout.strip()
                )

            if result.stderr:

                self.logger.write(
                    result.stderr.strip()
                )

            self.logger.write(
                f"RETURN CODE: {result.returncode}"
            )

            return CommandResult(
                command=command,
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr
            )

        except subprocess.TimeoutExpired:

            error = "Command timed out."

            self.logger.write(
                f"ERROR: {error}"
            )

            return CommandResult(
                command=command,
                returncode=124,
                stdout="",
                stderr=error
            )

    def terraform_init(
        self,
        directory,
        dry_run=True
    ):

        return self.run(
            ["terraform", "init"],
            cwd=directory,
            dry_run=dry_run
        )

    def terraform_plan(
        self,
        directory,
        dry_run=True
    ):

        return self.run(
            ["terraform", "plan"],
            cwd=directory,
            dry_run=dry_run
        )

    def terraform_apply(
        self,
        directory,
        dry_run=True
    ):

        return self.run(
            [
                "terraform",
                "apply",
                "-auto-approve"
            ],
            cwd=directory,
            dry_run=dry_run
        )

    def ansible_check(
        self,
        directory,
        dry_run=True
    ):

        return self.run(
            [
                "ansible-playbook",
                "playbook.yml",
                "--check"
            ],
            cwd=directory,
            dry_run=dry_run
        )