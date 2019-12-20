# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.plotter import esmdiag_plotter


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict], dict]
):
    """Generate python operator for `ploto.plotter.esmdiag_plotter` task.

    Parameters
    ----------
    task_id: str
        task name, should be unique in one DAG.
    params_generator: Callable[[dict, list], dict]
        a function to return params of `ploto.plotter.esmdiag_plotter.run_plotter` function.
        The function should has two parameters:
            drag_run_config: dict
                config set by trigger_run command

    Returns
    -------
    PythonOperator
        `ploto.plotter.esmdiag_plotter` task with task_id
    """
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
