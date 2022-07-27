# coding: utf-8
import importlib

from ploto.logger import get_logger

logger = get_logger()


def run_steps(steps, work_dir, config: dict or None = None) -> bool:
    for step in steps:
        _ = run_step(step=step, work_dir=work_dir, config=config)
    return True


def run_step(step, work_dir, config: dict or None = None) -> bool:
    step_module = get_step_module(step)
    if step_module is None:
        logger.error('step module is not found.')
        return False
    step_module.run_step(step=step, work_dir=work_dir, config=config)
    return True


def get_step_module(task: dict, config: dict or None = None):
    step_type = task['step_type']
    try:
        step_module = importlib.import_module('ploto.{step_type}'.format(step_type=step_type))
    except ImportError:
        logger.error('step type is not found: {step_type}'.format(step_type=step_type))
        return None
    return step_module
