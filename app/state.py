from datetime import datetime, timezone
from pathlib import Path
import json


class StateManager:

    def __init__(self, state_file="generated/state.json"):
        self.state_file = Path(state_file)

    def _load(self):
        if not self.state_file.exists():
            return {}

        try:
            return json.loads(
                self.state_file.read_text(
                    encoding="utf-8"
                )
            )

        except json.JSONDecodeError:
            return {}

    def save(self, **updates):

        self.state_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        state = self._load()

        state.update(updates)

        state["updated_at"] = datetime.now(
            timezone.utc
        ).isoformat()

        self.state_file.write_text(
            json.dumps(
                state,
                indent=2
            ),
            encoding="utf-8"
        )

        return state

    def load(self):
        return self._load()