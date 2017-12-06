# coding=utf-8


def draw_plot(plotter_task, work_dir, config):
    from gidat_plot.plotter.ncl_plotter import ncl_script_util
    from gidat_plot.plotter.ncldraw_plotter import ncldraw_util

    if plotter_task['type'] == 'ncl_plotter':
        ncl_script_util.run_plotter(plotter_task, work_dir)
    elif plotter_task['type'] == 'ncldraw_plotter':
        ncldraw_util.run_plotter(plotter_task, work_dir, config=config)
    else:
        print("plotter type is not supported:", plotter_task['type'])
