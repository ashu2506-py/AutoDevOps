from state import StateManager


state_manager = StateManager()

state_manager.save(
    project="auto-web-app",
    status="dry-run",
    operation="test",
    return_code=0
)

print(state_manager.load())