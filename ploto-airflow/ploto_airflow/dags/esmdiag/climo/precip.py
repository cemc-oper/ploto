# coding: utf-8
"""
Run the following command to test:
   airflow trigger_dag \
    --conf "$(jq '.' ./common_example.json)" \
    ploto_esmdiag_climo_precip

NOTE: jq is required to get json string from file.
"""
import airflow.utils.dates
from airflow.models import DAG

from ploto_airflow.esmdiag.climo.util import (
    generate_fetcher_params,
    generate_cdo_select_params,
    generate_gw_fetcher_params,
    generate_gw_cdo_select_params,
)
from ploto_airflow.operators.fetcher.edp_fecher import (
    generate_operator as generate_edp_fetcher_operator)
from ploto_airflow.operators.processor.cdo_processor.select import (
    generate_operator as generate_cdo_select_operator)

args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}

dag_id = "ploto_esmdiag_climo_precip"

with DAG(
        dag_id=dag_id,
        default_args=args,
        schedule_interval=None,
) as dag:
    fields = [
        'PRECT',
        'PRECC',
        'PRECL',
        'PS'
    ]
    fetch_data_step = generate_edp_fetcher_operator(
        "fetch_data",
        generate_fetcher_params,
        fields,
    )

    fetch_data_step.dag = dag

    select_steps = []

    for field in fields:
        select_data_step = generate_cdo_select_operator(
            f"select_data_{field}",
            generate_cdo_select_params,
            field
        )
        select_data_step.dag = dag
        select_data_step.set_upstream(fetch_data_step)
        select_steps.append(select_data_step)

    # gw
    gw_fetch_data_step = generate_edp_fetcher_operator(
        "fetch_gw",
        generate_gw_fetcher_params,
        ["gw"],
    )
    gw_fetch_data_step.dag = dag

    gw_select_step = generate_cdo_select_operator(
        "select_gw",
        generate_gw_cdo_select_params,
        "gw",
    )
    gw_select_step.dag = dag
    select_steps.append(gw_select_step)

    gw_select_step.set_upstream(gw_fetch_data_step)
