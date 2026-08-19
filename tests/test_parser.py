import pytest

from app.parser import load_yaml, ConfigError


def test_load_valid_yaml():
    data = load_yaml("configs/example.yaml")

    assert data["project"]["name"] == "auto-web-app"


def test_missing_file():

    with pytest.raises(ConfigError):
        load_yaml("configs/missing.yaml")


def test_invalid_extension(tmp_path):

    file = tmp_path / "config.txt"

    file.write_text("hello")

    with pytest.raises(ConfigError):
        load_yaml(str(file))


def test_invalid_yaml(tmp_path):

    file = tmp_path / "bad.yaml"

    file.write_text("project: [")

    with pytest.raises(ConfigError):
        load_yaml(str(file))


def test_empty_yaml(tmp_path):

    file = tmp_path / "empty.yaml"

    file.write_text("")

    with pytest.raises(ConfigError):
        load_yaml(str(file))
        
def test_yaml_top_level_list(tmp_path):

    file = tmp_path / "list.yaml"

    file.write_text(
        "- item1\n- item2"
    )

    with pytest.raises(ConfigError):
        load_yaml(str(file))