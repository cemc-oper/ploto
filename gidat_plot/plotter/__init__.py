# coding=utf-8


def draw_plot(plotter_task, work_dir, config):
    from gidat_plot.plotter.ncl_plotter import ncl_script_util
    from gidat_plot.plotter.ncldraw_plotter import ncldraw_util

    plotter_util_mapper = {
        'ncl_plotter': ncl_script_util,
        'ncldraw_plotter': ncldraw_util
    }

    plotter_type = plotter_task['type']
    plotter_util = plotter_util_mapper.get(plotter_type, None)

    if plotter_util:
        plotter_util.run_plotter(plotter_task, work_dir, config=config)
    else:
        print("plotter type is not supported:", plotter_task['type'])
