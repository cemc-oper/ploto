# coding: utf-8
from typing import Callable

from airflow.operators.python_operator import PythonOperator

from ploto_esmdiag.fetcher import edp_fetcher


def generate_operator(
        task_id: str,
        params_generator: Callable[[dict, list], dict],
        fields: list
) -> PythonOperator:
    """Generate python operator for `ploto.fetcher.edp_fetcher` task.

    Parameters
    ----------
    task_id: str
        task name, should be unique in one DAG.
    params_generator: Callable[[dict, list], dict]
        a function to return params of edp_fetcher.get_data function.
        The function should has two parameters:
            drag_run_config: dict
                config set by trigger_run command
            fields: list
                same as fields option.
    fields: list
        fields' name list.

    Returns
    -------
    PythonOperator
        `ploto.fetcher.edp_fetcher` task with task_id
    """
    def run_step(**context):
        drag_run_config = context["dag_run"].conf

        edp_fetcher.get_data(
            **params_generator(drag_run_config, fields)
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
