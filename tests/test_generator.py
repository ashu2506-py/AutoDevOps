from app.parser import load_yaml
from app.validator import validate_config
from app.generator import CodeGenerator


def get_config():

    data = load_yaml(
        "configs/example.yaml"
    )

    result = validate_config(data)

    assert result.valid is True

    return result.config


def test_terraform_generation(tmp_path):

    config = get_config()

    generator = CodeGenerator(
        output_dir=tmp_path
    )

    file = generator.generate_terraform(
        config
    )

    assert file.exists()

    content = file.read_text()

    assert "aws_instance" in content
    assert "aws_db_instance" in content
    assert "aws_vpc" in content


def test_ansible_generation(tmp_path):

    config = get_config()

    generator = CodeGenerator(
        output_dir=tmp_path
    )

    file = generator.generate_ansible(
        config
    )

    assert file.exists()

    content = file.read_text()

    assert "ansible.builtin.debug" in content


def test_kubernetes_generation(tmp_path):

    config = get_config()

    generator = CodeGenerator(
        output_dir=tmp_path
    )

    file = generator.generate_kubernetes(
        config
    )

    assert file.exists()

    content = file.read_text()

    assert "kind: Deployment" in content
    assert "kind: Service" in content