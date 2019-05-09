# coding: utf-8
import importlib

from ploto.logger import get_logger

logger = get_logger()


def get_step_module(task: dict, config: dict or None = None):
    step_type = task['step_type']
    try:
        step_module = importlib.import_module('ploto.{step_type}'.format(step_type=step_type))
    except ImportError:
        logger.error('step type is not found: {step_type}'.format(step_type=step_type))
        return None
    return step_module
