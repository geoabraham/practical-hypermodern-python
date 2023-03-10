"""Command-line interface."""
import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="es",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """
    Practical Hyper-modern Python
    """
    data = wikipedia.random_page(language=language)

    title = data.title
    extract = data.title

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
