# coding=utf-8
import json
import subprocess
import os

from ploto.logger import get_logger
logger = get_logger()


def save_ncl_script(ncl_script_path, ncl_script):
    with open(ncl_script_path, 'w') as f:
        f.write(ncl_script)


def run_plotter(plotter_task, work_dir, config):
    logger.info('prepare plot script...')
    ncl_script_content = plotter_task['ncl_script_content']
    image_path = plotter_task['image_path']

    param = {
        'ncl_script_path': 'draw.ncl',
        'ncl_params': plotter_task['ncl_params'],
        'image_path': image_path
    }
    save_ncl_script(param['ncl_script_path'], ncl_script_content)

    logger.info('running ncl...')

    ncl_pipe = subprocess.Popen(
        ['/home/wangdp/nwpc/gidat/plot/workspace/env/bin/python',
         os.path.join(os.path.dirname(__file__), 'ncl_script_plot.py'),
         '--param={param_string}'.format(param_string=json.dumps(param))],
        start_new_session=True
    )

    stdout, stderr = ncl_pipe.communicate()
    ncl_pipe.wait()
    ncl_pipe.terminate()

    # print(stdout)
    # print(stderr)

    logger.info('running ncl...done')
