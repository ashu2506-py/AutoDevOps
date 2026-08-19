from plugins.base import Plugin
from app.generator import CodeGenerator


class TerraformPlugin(Plugin):

    @property
    def name(self):
        return "terraform"

    @property
    def description(self):
        return "Terraform infrastructure generator"

    def generate(self, config):

        generator = CodeGenerator()

        return generator.generate_terraform(
            config
        )


class AnsiblePlugin(Plugin):

    @property
    def name(self):
        return "ansible"

    @property
    def description(self):
        return "Ansible playbook generator"

    def generate(self, config):

        generator = CodeGenerator()

        return generator.generate_ansible(
            config
        )


class KubernetesPlugin(Plugin):

    @property
    def name(self):
        return "kubernetes"

    @property
    def description(self):
        return "Kubernetes manifest generator"

    def generate(self, config):

        generator = CodeGenerator()

        return generator.generate_kubernetes(
            config
        )