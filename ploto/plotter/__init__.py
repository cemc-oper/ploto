# coding=utf-8
from ploto.logger import get_logger
from ploto.plotter import (
    ncl_plotter,
    ncldraw_plotter,
    esmdiag_plotter
)


plotter_util_mapper = {
    'ncl_plotter': ncl_plotter,
    'ncldraw_plotter': ncldraw_plotter,
    'esmdiag_plotter': esmdiag_plotter,
}

logger = get_logger()


def draw_plot(plotter_task, work_dir, config):
    plotter_type = plotter_task['type']
    plotter_util = plotter_util_mapper.get(plotter_type, None)

    if plotter_util:
        plotter_util.run_plotter(plotter_task, work_dir, config=config)
    else:
        logger.warn("plotter type is not supported:", plotter_task['type'])
