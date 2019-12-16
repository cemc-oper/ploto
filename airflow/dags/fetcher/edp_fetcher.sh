#!/usr/bin/env bash
set -x
#source ~/start_pyenv.sh
#pyenv activate ploto-env
python /home/hujk/ploto/ploto/airflow/dags/fetcher/run_edp_fetcher.py --step-config "$1"