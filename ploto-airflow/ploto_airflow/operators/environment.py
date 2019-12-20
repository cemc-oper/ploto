# coding: utf-8
import os

from airflow.operators.python_operator import PythonOperator


def generate_create_dir_operator(task_id):
    """Generate python operator to create a dir.

    Parameters
    ----------
    task_id: str
        task name, should be unique in one DAG.

    Returns
    -------
    PythonOperator
        create dir task with task_id
    """
    def run_step(**context):
        drag_run_config = context["dag_run"].conf
        work_dir = drag_run_config["work_dir"]

        try:
            os.makedirs(work_dir)
        except FileExistsError as e:
            pass

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )
    return airflow_task
