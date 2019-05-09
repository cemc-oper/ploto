# coding=utf-8
"""
edp_fetcher

Fetch data from EDP - Earth Data Platform
"""
import pathlib
import subprocess
import json


def download_edp_fetcher(file_task, work_dir, config):
    """

    :param file_task: ddps file task config
        {
            'type': 'edp',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': 'gamil_test',
                'date_range': ['19810101', '20140401'],
                'field_names': [
                    'AREI', 'AREL', 'AWNC', 'AWNI', 'CCN3', 'CLDICE', 'CLDLIQ', 'CLDST', 'CLOUD', 'CME', 'CMFDQ',
                    'CMFDT', 'CONCLD', 'DCQ', 'DTCOND', 'DTH', 'DTV', 'EFFICE', 'EFFLIQ', 'FICE'
                ],
                'datedif': 'h0',
                'lat_index': (0, 80),
                'lon_index': (0, 180),
                'lev_index': (0, 26)
            }
        }
    :param work_dir:
    :param config:
    """
    query_param = file_task['query_param']
    query_param['output_dir'] = str(pathlib.Path(work_dir, query_param['output_dir']))

    query_string = json.dumps(query_param)

    edp_script = config['edp_fetcher']['edp_script']

    edp_pipe = subprocess.Popen(
        [edp_script,
         query_string],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = edp_pipe.communicate()
    stdout = stdout.decode('utf-8').strip()
    print(stdout, stderr)
    edp_pipe.wait()
    edp_pipe.terminate()


def get_data(task, work_dir, config):
    download_edp_fetcher(task, work_dir, config)
