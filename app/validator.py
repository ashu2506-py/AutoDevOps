from pydantic import ValidationError

from app.models import InfrastructureConfig


class ValidationResult:
    def __init__(self, valid, errors=None, config=None):
        self.valid = valid
        self.errors = errors or []
        self.config = config


def validate_config(data):
    try:
        config = InfrastructureConfig(**data)

        errors = []

        if not config.resources:
            errors.append("At least one resource is required.")

        supported_types = {
            "compute",
            "database",
            "network"
        }

        for name, resource in config.resources.items():
            resource_type = resource.get("type")

            if resource_type not in supported_types:
                errors.append(
                    f"Resource '{name}' has unsupported type "
                    f"'{resource_type}'."
                )

        if errors:
            return ValidationResult(
                valid=False,
                errors=errors
            )

        return ValidationResult(
            valid=True,
            config=config
        )

    except ValidationError as error:
        errors = []

        for item in error.errors():
            errors.append(item["msg"])

        return ValidationResult(
            valid=False,
            errors=errors
        )