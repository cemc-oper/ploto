# coding: utf-8
import importlib
from ploto.logger import get_logger


def run_task(task, work_dir, config):
    logger = get_logger()
    metric = task['metric']
    figure = task["figure"]
    try:
        figure_module = importlib.import_module(
            "ploto_esmdiag.plotter.esmdiag_plotter.metrics.{metric}.figures.{figure}".format(
                metric=metric,
                figure=figure
            ), __package__)
    except ImportError:
        logger.error("can't found metric {metric} figure {figure}".format(
            metric=metric,
            figure=figure))
        return False

    ncl_script_path = getattr(figure_module, "NCL_SCRIPT_PATH")

    from ploto_esmdiag.plotter.esmdiag_plotter.figure_task import draw_figures
    draw_figures(ncl_script_path, task, work_dir, config)
    return True
