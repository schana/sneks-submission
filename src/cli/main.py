"""CLI for running and validating Sneks locally."""

import pathlib

import typer
from sneks.engine.config.graphics import GraphicsConfig
from sneks.engine.validator import main as validator
from sneks.games.classic import world
from sneks.games.classic.config import ClassicConfig

from submission import submission

app = typer.Typer(no_args_is_help=True, help="Local development tools for Sneks.")
PREFIX = str(pathlib.Path(submission.__file__).resolve().parent)


@app.command()
def run(
    runs: int = typer.Option(1, help="Number of game runs to execute."),
    sneks_count: int = typer.Option(1, help="Number of Sneks to spawn."),
    step_delay: int = typer.Option(40, help="Delay in ms between steps."),
    step_keypress_wait: bool = typer.Option(
        False, help="Wait for keypress between steps."
    ),
    end_delay: int = typer.Option(1000, help="Delay in ms after run ends."),
    end_keypress_wait: bool = typer.Option(
        False, help="Wait for keypress after run ends."
    ),
) -> None:
    """Run your Snek locally to test its behavior."""
    ClassicConfig(
        registrar_prefix=PREFIX,
        runs=runs,
        registrar_submission_sneks=sneks_count,
        graphics=GraphicsConfig(
            step_delay=step_delay,
            step_keypress_wait=step_keypress_wait,
            end_delay=end_delay,
            end_keypress_wait=end_keypress_wait,
        ),
    )
    world.main()


@app.command()
def validate() -> None:
    """Validate your Snek for submission."""
    validator.main(test_path=PREFIX)


def main() -> None:
    app()
