# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.plotter import esmdiag_plotter


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict], dict]
):
    def run_step(**context):
        drag_run_config = context["dag_run"].conf

        esmdiag_plotter.run_plotter(
            **params_generator(drag_run_config)
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
