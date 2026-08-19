import typer

from app.parser import load_yaml, ConfigError
from app.validator import validate_config
from app.generator import CodeGenerator

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

        output_file = generator.generate_terraform(
            result.config
        )

        typer.echo(
            f"Terraform generated successfully: {output_file}"
        )

    except ConfigError as error:

        typer.echo(
            f"ERROR: {error}",
            err=True
        )

        raise typer.Exit(code=1)
if __name__ == "__main__":
    app()