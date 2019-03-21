# coding=utf-8
from ploto.logger import get_logger


def draw_plot(plotter_task, work_dir, config):
    logger = get_logger()
    from ploto.plotter.ncl_plotter import ncl_script_util
    from ploto.plotter.ncldraw_plotter import ncldraw_util
    from ploto.plotter.esmdiag_plotter import esmdiag_util

    plotter_util_mapper = {
        'ncl_plotter': ncl_script_util,
        'ncldraw_plotter': ncldraw_util,
        'esmdiag_plotter': esmdiag_util,
    }

    plotter_type = plotter_task['type']
    plotter_util = plotter_util_mapper.get(plotter_type, None)

    if plotter_util:
        plotter_util.run_plotter(plotter_task, work_dir, config=config)
    else:
        logger.info("plotter type is not supported:", plotter_task['type'])
