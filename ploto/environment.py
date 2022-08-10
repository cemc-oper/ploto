import uuid
import os
import json
import datetime
import shutil
from typing import Dict, Union
from pathlib import Path

from ploto.logger import get_logger


logger = get_logger()


def get_work_dir(config: Dict) -> Path:
    base_config = config['base']
    run_base_dir = Path(base_config['run_base_dir'])

    temp_string = str(uuid.uuid4())
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    temp_directory = f"{current_datetime}_{temp_string}"
    os.chdir(run_base_dir)
    work_dir = Path(run_base_dir, temp_directory)
    try:
        work_dir.mkdir(parents=True)
    except FileExistsError as e:
        logger.warn('directory already exists:', work_dir)
    return work_dir


def store_base_environment() -> Dict:
    root_dir = os.getcwd()
    return {
        'root_dir': root_dir
    }


def prepare_environment(config: Dict) -> Path:
    return get_work_dir(config)


def enter_environment(work_dir: Path):
    os.chdir(work_dir)


def recovery_base_environment(base_env: Dict):
    os.chdir(base_env['root_dir'])


def clear_environment(work_dir: Path, config: Dict):
    if (
            "base" in config
            and "environment" in config["base"]
            and "clear_work_dir" in config["base"]["environment"]
            and config["base"]["environment"]["clear_work_dir"]
    ):
        logger.debug(f"deleting work directory: {work_dir}")
        shutil.rmtree(work_dir, ignore_errors=False)


def save_task_message(message_data: Dict):
    with open('message.json', 'w') as f:
        content = json.dumps(message_data, indent=2)
        f.write(content)
