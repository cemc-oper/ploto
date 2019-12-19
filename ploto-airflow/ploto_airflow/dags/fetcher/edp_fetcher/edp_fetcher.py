# coding: utf-8
"""
This is a test DAG to get data using edp fetcher. Python operator is used.

Run the following command to test:
   airflow trigger_dag \
    --conf "$(jq '.' ./example.json)" \
    ploto_fetcher_edp_fetcher

NOTE: jq is required to get json string from file.
"""
import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

from ploto_airflow.fetcher.edp_fecher import generate_operator as generate_edp_fetcher_operator


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
    show_task = BashOperator(
        task_id="show_date",
        bash_command='date',
        dag=dag,
    )

    run_task_id = "run_dep_fetcher"
    run_task = generate_edp_fetcher_operator(run_task_id)
    run_task.dag = dag

    run_task.set_upstream(show_task)
