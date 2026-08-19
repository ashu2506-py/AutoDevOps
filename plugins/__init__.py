from plugins.registry import PluginRegistry
from plugins.builtin import (
    TerraformPlugin,
    AnsiblePlugin,
    KubernetesPlugin,
)


def create_default_registry():

    registry = PluginRegistry()

    registry.register(
        TerraformPlugin()
    )

    registry.register(
        AnsiblePlugin()
    )

    registry.register(
        KubernetesPlugin()
    )

    return registry