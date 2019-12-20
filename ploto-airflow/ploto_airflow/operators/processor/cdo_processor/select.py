# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto.processor.cdo_processor.select import run_cdo


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict, str], dict],
        field: str
):
    """Generate python operator for `ploto.processor.cdo_processor.select` task.

    Parameters
    ----------
    task_id: str
        task name, should be unique in one DAG.
    params_generator: Callable[[dict, list], dict]
        a function to return params of `ploto.processor.cdo_processor.select.run_cdo` function.
        The function should has two parameters:
            drag_run_config: dict
                config set by trigger_run command
            field: str
                field name
    field: str
        field name

    Returns
    -------
    PythonOperator
        `ploto.processor.cdo_processor.select` task with task_id
    """
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
