from pathlib import Path
import yaml


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


def load_yaml(file_path: str) -> dict:
    path = Path(file_path)

    # Check whether the file exists
    if not path.exists():
        raise ConfigError(f"Configuration file not found: {path}")

    # Check file extension
    if path.suffix.lower() not in [".yaml", ".yml"]:
        raise ConfigError("Configuration file must be a YAML file.")

    try:
        # Open and read YAML file
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

    except yaml.YAMLError as error:
        raise ConfigError(f"Invalid YAML syntax: {error}")

    except OSError as error:
        raise ConfigError(f"Unable to read configuration: {error}")

    # Empty file
    if data is None:
        raise ConfigError("Configuration file is empty.")

    # YAML must contain an object/dictionary
    if not isinstance(data, dict):
        raise ConfigError("Top-level YAML structure must be a dictionary.")

    return data