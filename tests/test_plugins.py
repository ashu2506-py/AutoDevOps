from plugins import create_default_registry
from app.parser import load_yaml
from app.validator import validate_config


def get_config():

    data = load_yaml(
        "configs/example.yaml"
    )

    result = validate_config(data)

    assert result.valid is True

    return result.config


def test_default_plugins():

    registry = create_default_registry()

    assert "terraform" in registry.names()
    assert "ansible" in registry.names()
    assert "kubernetes" in registry.names()


def test_get_plugin():

    registry = create_default_registry()

    plugin = registry.get(
        "terraform"
    )

    assert plugin is not None
    assert plugin.name == "terraform"


def test_missing_plugin():

    registry = create_default_registry()

    assert registry.get(
        "does-not-exist"
    ) is None


def test_plugin_generation(tmp_path):

    config = get_config()

    registry = create_default_registry()

    terraform = registry.get(
        "terraform"
    )

    # Plugin uses the normal generator output.
    file = terraform.generate(config)

    assert file.exists()