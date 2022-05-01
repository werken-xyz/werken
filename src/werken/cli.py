from . import tids
from pathlib import Path
import click


def new_path(base, locale):
    while 1:
        tid = tids.random_id()
        path = base.joinpath(locale, tid[:2], f"{tid}.term")
        try:
            path.parent.mkdir(parents=True)
            path.touch(exist_ok=False)
        except FileExistsError:
            continue
        return path


@click.command()
@click.option('--locale', default='en')
def new_term(locale):
    base = Path.cwd().joinpath('data')
    if not base.exists():
        raise click.UsageError(
            "The 'data' path doesn't exist in the current directory")
    click.edit(filename=new_path(base, locale))
