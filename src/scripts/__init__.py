import pathlib

from sneks.config.config import config
from sneks.engine import runner
from sneks.validator import main as validator

import submission

prefix = str(pathlib.Path(submission.__file__).resolve().parent)


def validate():
    validator.main(test_path=prefix)


def run():
    config.registrar_prefix = prefix
    runner.main()
