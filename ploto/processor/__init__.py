import importlib
from typing import Dict, Protocol, runtime_checkable, Union
from pathlib import Path

from ploto.logger import get_logger


logger = get_logger()


@runtime_checkable
class Processor(Protocol):
    def run_processor(self, task: Dict, work_dir: Union[Path, str], config: Dict):
        ...


def run_step(step: Dict, work_dir: Union[Path, str], config: Dict):
    processor_type = step['type']
    try:
        processor_module = importlib.import_module(processor_type)
    except ImportError:
        logger.error(f"processor type is not found: {processor_type}")
        return

    if not isinstance(processor_module, Processor):
        raise TypeError(f"processor type is not a valid processor module: {processor_type}")

    processor_module.run_processor(task=step, work_dir=work_dir, config=config)
