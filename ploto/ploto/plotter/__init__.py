# coding=utf-8
import importlib

from ploto.logger import get_logger

logger = get_logger()


def run_step(step, work_dir, config):
    plotter_type = step['type']

    try:
        plotter_module = importlib.import_module('{plotter_type}'.format(plotter_type=plotter_type))
    except ImportError:
        logger.error("plotter type is not supported: {plotter_type}".format(plotter_type=plotter_type))
        return

    plotter_module.run_plotter(
        task=step,
        work_dir=work_dir,
        config=config)
