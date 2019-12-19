# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.fetcher import edp_fetcher


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict], dict]
):
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
