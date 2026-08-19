from executor import Executor


executor = Executor()

result = executor.run(
    ["terraform", "apply"],
    dry_run=True
)

print()
print("Return code:", result.returncode)
print("Skipped:", result.skipped)
print("Output:", result.stdout)