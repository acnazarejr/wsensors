"""utils file"""

import os
import typing

def list_files_by_extension(path: str, extension: str = None) -> typing.List[str]:
    """recusvie list files by a extension"""
    files: typing.List[str] = []
    for path, _, listed_files in os.walk(path):
        for name in listed_files:
            if extension is None or name.endswith(extension):
                files.append(os.path.join(path, name))
    return files
