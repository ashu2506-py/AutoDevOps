import typer
from plugins import create_default_registry
from app.parser import load_yaml, ConfigError
from app.validator import validate_config
from app.generator import CodeGenerator
from pathlib import Path
from app.executor import Executor
from app.logger import DeploymentLogger
from app.state import StateManager
from app.cost import estimate_monthly_cost
app = typer.Typer(
    name="autodevops",
    help="AutoDevOps - Infrastructure as Code Generator & Cloud Deployer"
)


@app.callback()
def main():
    """AutoDevOps CLI application."""
    pass


@app.command()
def hello():
    """Check whether AutoDevOps is running."""
    typer.echo("AutoDevOps is running!")


@app.command()
def validate(
    config: str = typer.Argument(
        ...,
        help="Path to the YAML configuration file"
    )
):
    """Validate a YAML infrastructure configuration."""

    try:
        data = load_yaml(config)

        result = validate_config(data)

        if not result.valid:
            typer.echo("Configuration is invalid:", err=True)

            for error in result.errors:
                typer.echo(f"  - {error}", err=True)

            raise typer.Exit(code=1)

        typer.echo("Configuration is valid.")
        typer.echo(f"Project: {result.config.project.name}")
        typer.echo(f"Provider: {result.config.project.provider}")
        typer.echo(f"Region: {result.config.project.region}")
        typer.echo(
            f"Resources found: {len(result.config.resources)}"
        )

    except ConfigError as error:
        typer.echo(f"ERROR: {error}", err=True)
        raise typer.Exit(code=1)
@app.command()
def generate(
    config: str = typer.Argument(
        ...,
        help="Path to the YAML configuration file"
    )
):
    """Generate Terraform infrastructure code."""

    try:
        data = load_yaml(config)

        result = validate_config(data)

        if not result.valid:

            typer.echo(
                "Configuration is invalid:",
                err=True
            )

            for error in result.errors:
                typer.echo(
                    f"  - {error}",
                    err=True
                )

            raise typer.Exit(code=1)

        generator = CodeGenerator()

        terraform_file = generator.generate_terraform(
            result.config
        )

        ansible_file = generator.generate_ansible(
            result.config
        )
        kubernetes_file = generator.generate_kubernetes(
            result.config
        )

        typer.echo(
            f"Terraform generated successfully: {terraform_file}"
        )

        typer.echo(
            f"Ansible generated successfully: {ansible_file}"
        )
        
        typer.echo(
            f"Kubernetes generated successfully: {kubernetes_file}"
        )

    except ConfigError as error:

        typer.echo(
            f"ERROR: {error}",
            err=True
        )
@app.command()
def plan(
    config: str = typer.Argument(
        ...,
        help="Path to the YAML configuration file"
    )
):
    """Generate Terraform and run a safe Terraform plan."""

    try:
        data = load_yaml(config)

        result = validate_config(data)

        if not result.valid:

            typer.echo(
                "Configuration is invalid:",
                err=True
            )

            for error in result.errors:
                typer.echo(
                    f"  - {error}",
                    err=True
                )

            raise typer.Exit(code=1)

        generator = CodeGenerator()

        terraform_file = generator.generate_terraform(
            result.config
        )

        terraform_directory = terraform_file.parent

        typer.echo(
            f"Terraform generated: {terraform_file}"
        )

        executor = Executor()

        init_result = executor.terraform_init(
            terraform_directory,
            dry_run=True
        )

        plan_result = executor.terraform_plan(
            terraform_directory,
            dry_run=True
        )

        # Save state
        state_manager = StateManager()

        state_manager.save(
            project=result.config.project.name,
            operation="plan",
            status="dry-run",
            generated_file=str(terraform_file),
            return_code=plan_result.returncode
        )

        typer.echo("")
        typer.echo("Terraform Plan")
        typer.echo("----------------")

        typer.echo(init_result.stdout)
        typer.echo(plan_result.stdout)

        typer.echo("")
        typer.echo("Plan completed in DRY-RUN mode.")
        typer.echo("State saved successfully.")

    except ConfigError as error:

        typer.echo(
            f"ERROR: {error}",
            err=True
        )

        raise typer.Exit(code=1)
@app.command()
def deploy(
    config: str = typer.Argument(
        ...,
        help="Path to the YAML configuration file"
    )
):
    """Generate infrastructure and perform a safe deployment simulation."""

    try:
        data = load_yaml(config)

        result = validate_config(data)

        if not result.valid:

            typer.echo(
                "Configuration is invalid:",
                err=True
            )

            for error in result.errors:
                typer.echo(
                    f"  - {error}",
                    err=True
                )

            raise typer.Exit(code=1)

        generator = CodeGenerator()

        terraform_file = generator.generate_terraform(
            result.config
        )

        terraform_directory = terraform_file.parent

        typer.echo(
            f"Terraform generated: {terraform_file}"
        )

        executor = Executor()

        init_result = executor.terraform_init(
            terraform_directory,
            dry_run=True
        )

        apply_result = executor.terraform_apply(
            terraform_directory,
            dry_run=True
        )

        # Save deployment state
        state_manager = StateManager()

        state_manager.save(
            project=result.config.project.name,
            operation="deploy",
            status="dry-run",
            generated_file=str(terraform_file),
            return_code=apply_result.returncode
        )

        typer.echo("")
        typer.echo("Deployment")
        typer.echo("----------------")

        typer.echo(init_result.stdout)
        typer.echo(apply_result.stdout)

        typer.echo("")
        typer.echo(
            "Deployment simulation completed safely."
        )
        typer.echo("State saved successfully.")

    except ConfigError as error:

        typer.echo(
            f"ERROR: {error}",
            err=True
        )

        raise typer.Exit(code=1)
@app.command()
def logs():
    """Show deployment logs."""

    logger = DeploymentLogger()

    typer.echo(
        logger.read()
    )
@app.command()
def status():
    """Show the latest AutoDevOps deployment state."""

    state_manager = StateManager()

    state = state_manager.load()

    if not state:
        typer.echo("No deployment state found.")
        return

    typer.echo("AutoDevOps Status")
    typer.echo("-----------------")

    for key, value in state.items():
        typer.echo(f"{key}: {value}")
        
@app.command()
def estimate(
    config: str = typer.Argument(
        ...,
        help="Path to the YAML configuration file"
    )
):
    """Estimate monthly infrastructure cost."""

    try:

        data = load_yaml(config)

        result = validate_config(data)

        if not result.valid:

            typer.echo(
                "Configuration is invalid:",
                err=True
            )

            for error in result.errors:

                typer.echo(
                    f"  - {error}",
                    err=True
                )

            raise typer.Exit(code=1)

        total, details = estimate_monthly_cost(
            result.config
        )

        typer.echo(
            "Estimated Monthly Cost"
        )

        typer.echo(
            "-----------------------"
        )

        for name, cost in details:

            typer.echo(
                f"{name}: ${cost:.2f}/month"
            )

        typer.echo(
            "-----------------------"
        )

        typer.echo(
            f"Estimated Total: ${total:.2f}/month"
        )

        typer.echo(
            ""
        )

        typer.echo(
            "Note: This is a demonstration estimate, "
            "not live cloud pricing."
        )

    except ConfigError as error:

        typer.echo(
            f"ERROR: {error}",
            err=True
        )
        raise typer.Exit(code=1)
    
@app.command()
def plugins():
    """List available AutoDevOps plugins."""

    registry = create_default_registry()

    typer.echo("Available Plugins")
    typer.echo("-----------------")

    for plugin in registry.all():

        typer.echo(
            f"{plugin.name}: {plugin.description}"
        )
if __name__ == "__main__":
    app()