from app.state import StateManager


def test_save_and_load_state(tmp_path):

    state_file = (
        tmp_path /
        "state.json"
    )

    manager = StateManager(
        state_file
    )

    manager.save(
        project="demo",
        status="dry-run"
    )

    state = manager.load()

    assert state["project"] == "demo"
    assert state["status"] == "dry-run"


def test_missing_state(tmp_path):

    manager = StateManager(
        tmp_path / "state.json"
    )

    assert manager.load() == {}


def test_corrupt_state(tmp_path):

    state_file = (
        tmp_path /
        "state.json"
    )

    state_file.write_text(
        "{invalid json"
    )

    manager = StateManager(
        state_file
    )

    assert manager.load() == {}