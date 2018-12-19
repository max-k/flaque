# coding: utf8

from .cli import cli


def main() -> None:
    cli(auto_envvar_prefix="FLAQUE")  # noqa: @pylint
