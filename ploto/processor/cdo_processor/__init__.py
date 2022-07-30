"""
cdo processor

Run cdo command.

task schema:
    {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'operator',
        ...
    }
"""
import importlib
from typing import Dict
from pathlib import Path

from ploto.logger import get_logger


def run_processor(task: Dict, work_dir: Path, config: Dict):
    logger = get_logger()
    cdo_operator = task['operator']
    try:
        operator_module = importlib.import_module(f".{cdo_operator}", __package__)
    except ImportError:
        logger.error(f"cdo operator not supported: {cdo_operator}")
        return False
    operator_module.run_cdo(task, work_dir, config)
    return True
