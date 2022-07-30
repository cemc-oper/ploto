import os
import importlib
from pathlib import Path
from typing import Union, Dict, Protocol, runtime_checkable

from ploto.logger import get_logger
from ploto.fetcher import ftp_fetcher, local_fetcher


logger = get_logger()


@runtime_checkable
class Fetcher(Protocol):
    def get_data(self, task, work_dir, config):
        ...


def run_step(step: Dict, work_dir: Union[Path, str], config: Dict):
    os.chdir(work_dir)
    fetcher_type = step['type']
    try:
        fetcher = importlib.import_module(fetcher_type)
    except ImportError:
        logger.error(f"fetcher type is not found: {fetcher_type}")
        return
    if not isinstance(fetcher, Fetcher):
        raise TypeError(f"fetcher type is not a valid fetcher module: {fetcher_type} ")

    fetcher.get_data(task=step, work_dir=work_dir, config=config)
