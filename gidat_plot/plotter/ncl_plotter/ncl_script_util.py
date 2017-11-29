# coding=utf-8
import json
import subprocess


def save_ncl_script(ncl_script_path, ncl_script):
    with open(ncl_script_path, 'w') as f:
        f.write(ncl_script)


def run_plotter(plotter_config, work_dir):
    print('prepare plot script...')
    ncl_script_content = plotter_config['ncl_script_content']
    image_path = plotter_config['image_path']

    param = {
        'ncl_script_path': 'draw.ncl',
        'ncl_params': plotter_config['ncl_params'],
        'image_path': image_path
    }
    save_ncl_script(param['ncl_script_path'], ncl_script_content)

    print('running ncl...')

    ncl_pipe = subprocess.Popen(
        ['/home/wangdp/nwpc/gidat/plot/workspace/env/bin/python',
         '/home/wangdp/nwpc/gidat/plot/workspace/gidat-plot/gidat_plot/plotter/ncl_plotter/ncl_script_plot.py',
         '--param={param_string}'.format(param_string=json.dumps(param))],
        start_new_session=True
    )

    stdout, stderr = ncl_pipe.communicate()
    ncl_pipe.wait()
    ncl_pipe.terminate()

    # print(stdout)
    # print(stderr)

    print('running ncl...done')
