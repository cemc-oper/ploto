import importlib
from typing import Dict, Union, Optional, Protocol, runtime_checkable
from pathlib import Path

from ploto.logger import get_logger


logger = get_logger()


def run_steps(steps: Dict, work_dir: Union[Path, str], config: Optional[Dict] = None) -> bool:
    for step in steps:
        _ = run_step(step=step, work_dir=work_dir, config=config)
    return True


def run_step(step: Dict, work_dir: Union[Path, str], config: Optional[Dict] = None) -> bool:
    step_module = get_step_module(step)
    if step_module is None:
        logger.error('step module is not found.')
        return False
    step_module.run_step(step=step, work_dir=work_dir, config=config)
    return True


@runtime_checkable
class Step(Protocol):
    def run_step(self, step: Dict, work_dir: Union[Path, str], config: Dict):
        ...


def get_step_module(task: Dict, config: Optional[Dict] = None) -> Optional[Step]:
    step_type = task['step_type']
    try:
        step_module = importlib.import_module(f'ploto.{step_type}')
    except ImportError:
        logger.error(f'step type is not found: {step_type}')
        return None

    if isinstance(step_module, Step):
        logger.error(f"step type is not a valid step module: {step_type}")
        return None

    return step_module
