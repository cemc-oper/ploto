# coding: utf-8
"""
use python operator, command:
   airflow trigger_dag \
    --conf '{"step_config":"{\"work_dir\": \"/home/hujk/clusterfs/wangdp/temp\"}"}' \
    ploto_fetcher_edp_fetcher_py
"""

import json

import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from ploto.fetcher import edp_fetcher


def run_edp_fetcher_step(**context):
    drag_run_config = context["dag_run"].conf
    step_config = json.loads(drag_run_config['step_config'])
    # task = step_config["task"]
    work_dir = step_config["work_dir"]
    # config = step_config["config"]

    task = {
        'type': 'edp_fetcher',
        'query_param': {
            'type': 'nc',
            'output_dir': './data',
            'file_prefix': 'GAMIL.gamil_wu_run11',
            'date_range': ['19810101', '19820101'],
            'field_names': [
                'PRECT',
                'PRECC',
                'PRECL',
                'PS'
            ],
            'datedif': 'h0'
        }
    }

    # work_dir = "/home/hujk/clusterfs/wangdp/temp"

    config = {
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/pyProject/"
        }
    }

    edp_fetcher.get_data(
        task,
        work_dir,
        config=config
    )


args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}


dag = DAG(
    dag_id="ploto_fetcher_edp_fetcher_py",
    default_args=args,
    schedule_interval=None,
)

show_step = BashOperator(
    task_id="show_date",
    bash_command='date',
    dag=dag,
)


run_step = PythonOperator(
    task_id="run_dep_fetcher",
    provide_context=True,
    python_callable=run_edp_fetcher_step,
    dag=dag,
)

run_step.set_upstream(show_step)
