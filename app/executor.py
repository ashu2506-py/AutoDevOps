import shutil
import subprocess
from dataclasses import dataclass


@dataclass
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    skipped: bool = False


class Executor:

    def run(
        self,
        command,
        cwd=None,
        dry_run=True
    ):

        command = list(command)

        command_text = " ".join(command)

        print(f"Command: {command_text}")

        # Safe mode
        if dry_run:

            print("DRY-RUN: command was not executed.")

            return CommandResult(
                command=command,
                returncode=0,
                stdout="DRY-RUN: command was not executed.",
                stderr="",
                skipped=True
            )

        # Check whether command exists
        if shutil.which(command[0]) is None:

            error = f"Command not found: {command[0]}"

            print(error)

            return CommandResult(
                command=command,
                returncode=127,
                stdout="",
                stderr=error
            )

        try:

            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=600,
                check=False
            )

            return CommandResult(
                command=command,
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr
            )

        except subprocess.TimeoutExpired:

            return CommandResult(
                command=command,
                returncode=124,
                stdout="",
                stderr="Command timed out."
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