# coding: utf8

from .cli import cli


def main(*args, **kwargs) -> None:
    cli(*args, **kwargs, auto_envvar_prefix="FLAQUE")  # noqa: @pylint
