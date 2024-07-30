import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath) # handle the slashes, convert the path to the system (Windows, Linux...) syntax
    filedir, filename = os.path.split(filepath) # src/.../ would be the filedir and __init__.py would be the filename
    if filedir != "": 
        os.makedirs(filedir, exist_ok=True) # create the directories if they don't exist
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0): # check if the file exists or is empty
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filename}")          
    else:
        logging.info(f"File already exists: {filename} and is not empty.")   
    