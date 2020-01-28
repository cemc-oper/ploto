# coding: utf-8
import json
import os
from pathlib import Path
import warnings


def test_ncldraw_util():
    warnings.warn("ncldraw is no longer used in NWPC.", DeprecationWarning)
    from ploto_gidat.plotter.ncldraw_plotter import run_plotter

    work_dir = "/space/windroc/workspace/plot/playground/test_case_1"
    config = {}

    task_file_path = Path(Path(__file__).parent, "task.xml")
    with open(task_file_path) as task_file:
        task_content = task_file.read()

    plot_task = {
        'type': 'ploto_gidat.plotter.ncldraw_plotter',
        'task_files': [
            {
                'file_path': 'task.xml',
                'file_content': task_content
            }
        ],
        # 'resource_files': [
        #     {
        #         'file_path': 'fill.xml', # resource file path, NOTE: this is a relative path currently.
        #         'file_content': 'content' # resource file content
        #     }
        # ],
        'time_level': '2017071400084',
        'image_path': 'image.png',
    }

    print(json.dumps(plot_task, indent=2))

    run_plotter(plot_task, work_dir, config)


if __name__ == "__main__":
    current_dir = os.getcwd()
    test_ncldraw_util()
    os.chdir(current_dir)
