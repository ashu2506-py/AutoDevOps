from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from app.models import InfrastructureConfig


class CodeGenerator:

    def __init__(
        self,
        template_dir="templates",
        output_dir="generated"
    ):
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)

        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True
        )

    def generate_terraform(
        self,
        config: InfrastructureConfig
    ):

        template = self.env.get_template("main.tf.j2")

        output_file = (
            self.output_dir /
            "terraform" /
            "main.tf"
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file.write_text(
            template.render(
                config=config,
                resources=config.typed_resources()
            ),
            encoding="utf-8"
        )

        return output_file
    
    def generate_ansible(
            self,
            config: InfrastructureConfig
        ):

            template = self.env.get_template("playbook.yml.j2")

            output_file = (
                self.output_dir /
                "ansible" /
                "playbook.yml"
            )

            output_file.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            output_file.write_text(
                template.render(
                    config=config,
                    resources=config.typed_resources()
                ),
                encoding="utf-8"
            )

            return output_file