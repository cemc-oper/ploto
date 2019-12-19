# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.processor.cdo_processor.select import run_cdo


def generate_params(drag_run_config: dict, field: str) -> dict:
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    file_prefix = '{atm_id}.{case_id}'.format(
        atm_id=common_config['model_info']['atm_id'],
        case_id=common_config['case_info']['id']
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.monthly.{time_range}.nc"

    task_config = {
        'step_type': 'processor',
        'type': 'cdo_processor',
        'operator': 'select',
        'params': {
            'name': field,
            'startdate': common_config['date']['start'],
            'enddate': common_config['date']['end']
        },
        'input_files': [
            './data/{step1_file_prefix}.*.nc'.format(step1_file_prefix=step1_file_prefix)
        ],
        'output_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name=field,
        ),
    }
    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_operator(task_id: str, params_generator: Callable[[dict, str], dict], field: str):
    def run_step(**context):
        drag_run_config = context["dag_run"].conf

        run_cdo(
            **params_generator(drag_run_config, field)
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
