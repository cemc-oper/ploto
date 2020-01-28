# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto_esmdiag.processor.esmdiag_data_processor import run_processor


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict, list], dict],
        vinterp_tasks: list
):
    """Generate python operator for `ploto.processor.esmdiag_data_processor.vinterp` task.

    Parameters
    ----------
    task_id: str
        task name, should be unique in one DAG.
    params_generator: Callable[[dict, list], dict]
        a function to return params of `ploto.processor.cdo_processor.select.run_cdo` function.
        The function should has two parameters:
            drag_run_config: dict
                config set by trigger_run command
            vinterp_task: dict
                vinterp task list
    vinterp_tasks: list
        vinterp task list

    Returns
    -------
    PythonOperator
        `ploto.processor.esmdiag_data_processor.vinterp` task with task_id
    """
    def run_step(**context):
        drag_run_config = context["dag_run"].conf

        run_processor(
            **params_generator(drag_run_config, vinterp_tasks)
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
