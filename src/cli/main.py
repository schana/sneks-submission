import pathlib

import typer
from sneks.engine.config.graphics import GraphicsConfig
from sneks.engine.validator import main as validator
from sneks.games.classic import world
from sneks.games.classic.config import ClassicConfig

from submission import submission

app = typer.Typer(no_args_is_help=True)
PREFIX = str(pathlib.Path(submission.__file__).resolve().parent)


@app.command()
def run(
    runs: int = 1,
    sneks_count: int = 1,
    step_delay: int = 40,
    step_keypress_wait: bool = False,
    end_delay: int = 1000,
    end_keypress_wait: bool = False,
) -> None:
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
    validator.main(test_path=PREFIX)


def main() -> None:
    app()
