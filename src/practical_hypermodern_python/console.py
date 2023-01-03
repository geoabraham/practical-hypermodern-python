import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """
    Practical Hyper-modern Python
    """
    click.echo("Hello World !!!")
