#utils file use to create excepts also
#creating ready yml files also.

#creating model at here and will use in other files it is called utility functions

import os
import yaml
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations #to show alerts for type or return error espcialy if return type is int but you are getting string
from box import ConfigBox #confi box use to check yaml values y using . operator so we do not need to use [ operator check it easy way to access things]
from pathlib import Path
from typing import Any

@ensure_annotations #decorator
def read_yaml(path_to_yaml: Path) ->  ConfigBox:
    """
        This function is used to create ready yml files.
        :param path_to_yaml: Path to yaml file
        :return: Path to ready yaml file
    """
    """
        reads yaml file and retrns

        Args:
            path_to_yaml (str): Path like input

        Raises:
            ValueError: if yaml file is empty
            e: empty file
        Returns:
            ConfigBox: ConfigBox object
    """

    try:
        with open(path_to_yaml)as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
        

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"