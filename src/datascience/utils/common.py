import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigurationBox: ConfigurationBox type
    """

    try:
        with open(path_to_yaml,'r',encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories(list): list of path directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Defults to 
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_jason(path: Path, data: dict):
    """save json data

    Args:
        path (path): path to json file
        data(dict): data to save in json file
    """

    with open(path,"w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json data

    Args:
        path (path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
     Args:
        path (path): path to binary file
        data(Any): data to save in binary file

    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved to {path}")



@ensure_annotations
def load_bin(path: Path):
    """load binary file
     Args:
        path (path): path to binary file
    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data
    