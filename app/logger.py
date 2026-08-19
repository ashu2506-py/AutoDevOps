from datetime import datetime, timezone
from pathlib import Path


class DeploymentLogger:

    def __init__(self, log_file="generated/deployment.log"):
        self.log_file = Path(log_file)

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def write(self, message: str):

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        with self.log_file.open(
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"[{timestamp}] {message}\n"
            )

    def read(self):

        if not self.log_file.exists():
            return "No deployment logs found."

        return self.log_file.read_text(
            encoding="utf-8"
        )