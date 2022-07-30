import importlib
from typing import Dict, Union, Protocol, runtime_checkable
from pathlib import Path

from ploto.logger import get_logger


logger = get_logger()


@runtime_checkable
class Plotter(Protocol):
    def run_plotter(self, task: Dict, work_dir: Union[Path, str], config: Dict):
        ...


def run_step(step: Dict, work_dir: Union[Path, str], config: Dict):
    plotter_type = step['type']

    try:
        plotter_module = importlib.import_module(plotter_type)
    except ImportError:
        logger.error(f"plotter type is not found: {plotter_type}")
        return

    if not isinstance(plotter_module, Plotter):
        raise TypeError(f"plotter type is not a valid plotter module: {plotter_module} ")

    plotter_module.run_plotter(
        task=step,
        work_dir=work_dir,
        config=config)
