import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox #easier to access the yaml file (ex: dict.key instead of dict['key'])
from pathlib import Path
from typing import Any


@ensure_annotations #make sure the arguments respect the type they are given
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns 
    
    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox of the yaml file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from: {path_to_yaml}. Loaded the content successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"This yaml file is empty: {path_to_yaml}")
    except Exception as e:
        raise e
   
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
        
    Args:
        path_to_directories (list): list of directories
        verbose (bool, optional): print the directories. Defaults to True.
    """
    for path in path_to_directories: 
        os.makedirs(path, exist_ok=True)
        if verbose :
            logger.info(f"Created directory: {path}")
                


        