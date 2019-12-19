# coding: utf-8
import datetime
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.fetcher import edp_fetcher


def generate_params(drag_run_config: dict) -> dict:
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    file_prefix = '{atm_id}.{case_id}'.format(
        atm_id=common_config['model_info']['atm_id'],
        case_id=common_config['case_info']['id']
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    task_config = {
        'step_type': 'fetcher',
        'common': common_config,
        'type': 'edp_fetcher',
        'query_param': {
            'type': 'nc',
            'output_dir': './data',
            'file_prefix': step1_file_prefix,
            'date_range': date_range,
            'field_names': [
                'PRECT',
                'PRECC',
                'PRECL',
                'PS'
            ],
            'datedif': 'h0'
        },
    }
    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_operator(task_id: str, params_generator: Callable[[dict], dict]):
    def run_step(**context):
        drag_run_config = context["dag_run"].conf

        edp_fetcher.get_data(
            **params_generator(drag_run_config)
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
