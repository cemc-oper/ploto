import importlib
from typing import Union, Dict, Protocol, runtime_checkable
from pathlib import Path

from ploto.logger import get_logger


@runtime_checkable
class Distributor(Protocol):
    def run_distributor(self, task: Dict, work_dir: Union[Path, str], config: Dict):
        ...


logger = get_logger()


def run_step(step, work_dir, config):
    distributor_type = step['type']
    try:
        distributor_module = importlib.import_module(distributor_type)
    except ImportError:
        logger.error(f"distributor type not found: {distributor_type}")
        return

    if isinstance(distributor_module, Distributor):
        raise TypeError(f"distributor type is not a valid distributor module: {distributor_type}")

    distributor_module.run_distributor(task=step, work_dir=work_dir, config=config)
