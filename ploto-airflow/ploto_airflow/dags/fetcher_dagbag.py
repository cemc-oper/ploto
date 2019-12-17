# coding: utf-8
import pathlib

from airflow.models import DagBag

from ploto_airflow import MODULE_PATH


dag_dirs = [
    str(pathlib.Path(MODULE_PATH, "fetcher/edp_fetcher"))
]

for a_dir in dag_dirs:
    dag_bag = DagBag(a_dir)

    if dag_bag:
        for dag_id, dag in dag_bag.dags.items():
            globals()[dag_id] = dag
