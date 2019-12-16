# coding: utf-8
"""
use bash operator to run edp fetcher, command:
    airflow trigger_dag \
        --conf '{"step_config":"{\\\"work_dir\\\": \\\"/home/hujk/clusterfs/wangdp/temp\\\"}"}' \
        ploto_fetcher_edp_fetcher
"""

import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator


args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}


dag = DAG(
    dag_id="ploto_fetcher_edp_fetcher",
    default_args=args,
    schedule_interval=None,
)

show_step = BashOperator(
    task_id="show_date",
    bash_command='date',
    dag=dag,
)


run_step = BashOperator(
    task_id="run_dep_fetcher",
    bash_command='/home/hujk/ploto/ploto/airflow/dags/fetcher/edp_fetcher.sh "{{ dag_run.conf["step_config"] }}"',
    # bash_command='ls',
    dag=dag,
)

run_step.set_upstream(show_step)
