# coding: utf-8
from airflow.operators.python_operator import PythonOperator

from ploto.processor.cdo_processor.select import run_cdo


def generate_operator(task_id: str):
    def run_step(**context):
        drag_run_config = context["dag_run"].conf
        step_config = drag_run_config['step_config']

        task = step_config["task"]
        work_dir = step_config["work_dir"]
        config = step_config["config"]

        run_cdo(
            task,
            work_dir,
            config=config
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_step,
    )

    return airflow_task
