# coding: utf-8
import json
import os
from click.testing import CliRunner


def test_ncldraw_plot():
    from gidat_plot.plotter.ncldraw_plotter.ncldraw_plot import ncldraw_plot
    runner = CliRunner()

    param = {
        'task_file': 'task.xml',
        'time_level': '2017071400084',
    }
    param_string = json.dumps(param)

    result = runner.invoke(ncldraw_plot, [
        "--param="+param_string
    ])

    print(result)


if __name__ == "__main__":
    current_dir = os.getcwd()
    os.chdir("/space/windroc/workspace/plot/playground/test_case_1")
    test_ncldraw_plot()
    os.chdir(current_dir)
