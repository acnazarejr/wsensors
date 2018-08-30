"""sensorid cli main file"""

import click
from wsensors.common import utils
from wsensors.common import captures


@click.group(context_settings=dict(max_content_width=120, color=True))
@click.pass_context
def main(_ctx: click.Context) -> None:
    """sensorid command group"""
    pass


@main.command()
@click.option(
    '--input', '-i', 'input_path',
    type=click.Path(file_okay=False, exists=True, resolve_path=True, writable=True),
    required=True,
    metavar='<path>',
    help="Input captures folder"
)
def create_dataset(input_path: str) -> None:
    """Convert captures."""
    capture_zipped_files = utils.list_files_by_extension(input_path, 'zip')
    for capture_file in capture_zipped_files:
        subject_info = captures.get_subject_info(capture_file)
        captures.get_client_device_data(capture_file)
