# coding: utf-8
import importlib
from ploto.logger import get_logger


def run_task(task, work_dir, config):
    logger = get_logger()
    figure = task["figure"]
    try:
        figure_module = importlib.import_module(
            ".figures.{figure}".format(figure=figure), __package__)
    except ImportError:
        logger.error("can't found figure {figure}".format(figure=figure))
        return False

    ncl_script_path = getattr(figure_module, "NCL_SCRIPT_PATH")

    from ploto.plotter.esmdiag_plotter.metrics.climo.figure_task import draw_figures
    draw_figures(ncl_script_path, task, work_dir, config)
