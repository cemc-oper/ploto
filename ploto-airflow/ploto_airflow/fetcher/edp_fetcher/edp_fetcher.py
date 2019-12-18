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


with DAG(
    dag_id=dag_id,
    default_args=args,
    schedule_interval=None,
) as dag:
    show_step = BashOperator(
        task_id="show_date",
        bash_command='date',
        dag=dag,
    )

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

    run_step = PythonOperator(
        task_id="run_dep_fetcher",
        provide_context=True,
        python_callable=run_edp_fetcher_step,
        dag=dag,
    )

    run_step.set_upstream(show_step)
