from app.parser import load_yaml
from app.validator import validate_config


def test_load_valid_yaml():

    data = load_yaml(
        "configs/example.yaml"
    )

    result = validate_config(data)

    assert result.valid is True
    assert result.config.project.name == "auto-web-app"


def test_missing_project():

    data = {
        "resources": {
            "web": {
                "type": "compute"
            }
        }
    }

    result = validate_config(data)

    assert result.valid is False


def test_empty_resources():

    data = {
        "project": {
            "name": "demo"
        },
        "resources": {}
    }

    result = validate_config(data)

    assert result.valid is False


def test_invalid_resource_type():

    data = {
        "project": {
            "name": "demo"
        },
        "resources": {
            "rocket": {
                "type": "spaceship"
            }
        }
    }

    result = validate_config(data)

    assert result.valid is False


def test_multiple_invalid_resources():

    data = {
        "project": {
            "name": "demo"
        },
        "resources": {
            "rocket": {
                "type": "spaceship"
            },
            "robot": {
                "type": "robot"
            }
        }
    }

    result = validate_config(data)

    assert result.valid is False
    assert len(result.errors) == 2


def test_missing_project_name():

    data = {
        "project": {},
        "resources": {
            "web": {
                "type": "compute"
            }
        }
    }

    result = validate_config(data)

    assert result.valid is False