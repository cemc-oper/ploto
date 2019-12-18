# coding: utf-8
"""
use python operator, command:
   airflow trigger_dag \
    --conf "$(jq '.' ./edp_fetcher_example.json)" \
    ploto_fetcher_edp_fetcher

NOTE: jq is required to get json string from file.
"""
import json

import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from ploto.fetcher import edp_fetcher


args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}


dag_id = "ploto_fetcher_edp_fetcher"


def generate_operator(task_id: str):
    def run_edp_fetcher_step(**context):
        drag_run_config = context["dag_run"].conf
        step_config = drag_run_config['step_config']
        task = step_config["task"]
        work_dir = step_config["work_dir"]
        config = step_config["config"]

        edp_fetcher.get_data(
            task,
            work_dir,
            config=config
        )

    airflow_task = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=run_edp_fetcher_step,
    )

    return airflow_task


with DAG(
    dag_id=dag_id,
    default_args=args,
    schedule_interval=None,
) as dag:
    show_task = BashOperator(
        task_id="show_date",
        bash_command='date',
        dag=dag,
    )

    run_task_id = "run_dep_fetcher"
    run_task = generate_operator(run_task_id)
    run_task.dag = dag

    run_task.set_upstream(show_task)
