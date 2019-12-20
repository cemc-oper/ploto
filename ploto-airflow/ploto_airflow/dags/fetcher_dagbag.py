# coding: utf-8
"""A 'dagbag' for all enabled DAGs in this project.

WARNING
-------
this file does not working.
"""
import pathlib

from airflow.models import DagBag

from ploto_airflow import MODULE_PATH


dag_dirs = [
    str(pathlib.Path(MODULE_PATH, "fetcher/edp_fetcher")),
    str(pathlib.Path(MODULE_PATH, "fetcher/edp_fetcher_bash"))
]

for a_dir in dag_dirs:
    print(a_dir)
    dag_bag = DagBag(a_dir)

    if dag_bag:
        for dag_id, dag in dag_bag.dags.items():
            print(dag_id, dag)
            globals()[dag_id] = dag
