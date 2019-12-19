# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.processor.cdo_processor.select import run_cdo


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict, str], dict],
        field: str
):
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
