

import zipfile
import json

def __read_metadata(zipped_capture_file: str) -> dict:
    capture_file = zipfile.ZipFile(zipped_capture_file, 'r')
    capture_metadata_file = capture_file.open('capture.json')
    return json.load(capture_metadata_file)

def get_subject_info(zipped_capture_file: str) -> dict:
    """extract metadata from zipped capture file (sensorcap files)"""
    metadata = __read_metadata(zipped_capture_file)
    return metadata['subjectInfo']

def get_client_device_data(zipped_capture_file: str) -> dict:
    """extract sensor data from zipped capture file (sensorcap files)"""
    metadata = __read_metadata(zipped_capture_file)    
    client_device_info = metadata['clientDeviceData']
    print clie
