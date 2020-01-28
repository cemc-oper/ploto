# coding=utf-8
import pathlib
import os
import subprocess
import json


def save_ddps_param_file(ddps_param_file_path, param):
    with open(ddps_param_file_path, 'w') as f:
        content = json.dumps(param, indent=2)
        f.write(content)


def download_ddps_fetcher(file_task, work_dir, config):
    """

    :param file_task: ddps file task config
        {
            'type': 'ploto.fetcher.ddps_fetcher',
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
            },
            'file_name': 'data_file.grib2'
        }
    :param work_dir:
    :param config:

        {
            'ddps_fetcher': {
                'bsc_command': 'bsc command file path'
            }
        }
    """
    query_param = file_task['query_param']
    query_param['config']['savePath'] = str(pathlib.Path(work_dir, query_param['config']['savePath']))

    ddps_param_file_path = file_task['file_name'] + '.config'
    save_ddps_param_file(ddps_param_file_path, query_param)

    bsc_command = config['ddps_fetcher']['bsc_command']

    ddps_pipe = subprocess.Popen(
        [bsc_command,
         ddps_param_file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = ddps_pipe.communicate()
    stdout = stdout.decode('utf-8').strip()
    std_lines = stdout.split('\n')
    if len(std_lines) == 1:
        print('no data')
        if isinstance(stdout, bytes):
            stdout = stdout.decode('utf-8')
        if isinstance(stderr, bytes):
            stderr = stderr.decode('utf-8')
        print(stdout)
        print(stderr)
    elif len(std_lines) == 2:
        result_line = std_lines[1]
        file_list_str = result_line[len('ExtractResultList:['):-1]
        file_list = file_list_str.split(',')
        if len(file_list) == 1:
            os.rename(os.path.join(query_param['config']['savePath'], file_list[0]),
                      os.path.join(work_dir, file_task['file_name']))
        else:
            print(file_list)
            print("we don't support more than one file.")
    else:
        print('unknown error:', stdout)
    ddps_pipe.wait()
    ddps_pipe.terminate()


def get_data(task, work_dir, config):
    download_ddps_fetcher(task, work_dir, config)
