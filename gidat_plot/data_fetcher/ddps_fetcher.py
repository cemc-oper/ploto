# coding=utf-8
import pathlib
import os
import subprocess
import json


def save_ddps_param_file(ddps_param_file_path, param):
    with open(ddps_param_file_path, 'w') as f:
        content = json.dumps(param, indent=2)
        f.write(content)


def download_ddps_fetcher(file_task, work_dir):
    """

    file_task:

    {
        'type': 'ddps',
        'query_param': {
            "username":"admin",
            "password":"admin",
            "operation":"extractdownload",
            "config":{
                "date":"20140101",
                "groupname":"DYN",
                "expID":"G1600010",
                "time":"1200,12:00",
                "step":"0",
                "levtype":"pl",
                "param":"t",
                "levelist":"850",
                "savePath":"./ddps"
            }
        }
    }

    """
    query_param = file_task['query_param']
    query_param['config']['savePath'] = str(pathlib.Path(work_dir, query_param['config']['savePath']))

    ddps_param_file_path = 'ddps_param.config'
    save_ddps_param_file(ddps_param_file_path, query_param)

    ddps_pipe = subprocess.Popen(
        ['/home/wangdp/nwpc/gidat/data/ddps/BSC/bsc/bin/bsc',
         'ddps_param.config'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = ddps_pipe.communicate()
    stdout = stdout.decode('utf-8').strip()
    std_lines = stdout.split('\n')
    if len(std_lines) == 1:
        print('no data')
    elif len(std_lines) == 2:
        result_line = std_lines[1]
        file_list_str = result_line[len('ExtractResultList:['):-1]
        file_list = file_list_str.split(',')
        print(file_list)
    else:
        print('unknown error:', stdout)
    ddps_pipe.wait()
    ddps_pipe.terminate()


def get_data(file_task, work_dir):
    download_ddps_fetcher(file_task, work_dir)
