"""convert captures files from smartcap"""

import os
import click


@click.command()
@click.option(
    '--input', '-i', 'input_path',
    type=click.Path(file_okay=False, exists=True, resolve_path=True, writable=True),
    required=True,
    metavar='<path>',
    help="Input captures folder"
)
def convert(input_path: str) -> None:
    """Convert captures."""
    capture_raw_files: list = []
    for path, _, listed_files in os.walk(input_path):
        for name in listed_files:
            if name.endswith('.zip'):
                capture_raw_files.append(os.path.join(path, name))
    click.echo(f'The size of list is {len(capture_raw_files)}')


if __name__ == '__main__':
    convert()
