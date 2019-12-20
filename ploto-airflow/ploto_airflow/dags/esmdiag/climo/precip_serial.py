# coding: utf-8
"""ESMDIAG's climo/precip figure workflow which is serial.

WARNING
-------
This DAG is only for test.

Example
-------
Run the following command to test:

   $ airflow trigger_dag \
     --conf "$(jq '.' ./common_example.json)" \
     ploto_esmdiag_climo_precip_serial

NOTE: jq is required to get json string from file.
"""
import airflow.utils.dates
from airflow.models import DAG

from ploto_airflow.esmdiag.climo.util import (
    generate_fetcher_params,
    generate_cdo_select_params,
    generate_gw_fetcher_params,
    generate_gw_cdo_select_params,
    generate_plotter_params,
)
from ploto_airflow.operators.environment import generate_create_dir_operator
from ploto_airflow.operators.fetcher.edp_fecher import (
    generate_operator as generate_edp_fetcher_operator
)
from ploto_airflow.operators.processor.cdo_processor.select import (
    generate_operator as generate_cdo_select_operator
)
from ploto_airflow.operators.plotter.esmdiag_plotter import (
    generate_operator as generate_plotter_operator
)

args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}

dag_id = "ploto_esmdiag_climo_precip_serial"

with DAG(
        dag_id=dag_id,
        default_args=args,
        schedule_interval=None,
) as dag:
    # prepare environment
    create_dir_step = generate_create_dir_operator(
        "create_work_dir"
    )
    create_dir_step.dag = dag

    # fetch and process data
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
    fetch_data_step.set_upstream(create_dir_step)

    previous_step = fetch_data_step

    for field in fields:
        select_data_step = generate_cdo_select_operator(
            f"select_data_{field}",
            generate_cdo_select_params,
            field
        )
        select_data_step.dag = dag
        select_data_step.set_upstream(previous_step)
        previous_step = select_data_step

    # fetch and process gw
    gw_fetch_data_step = generate_edp_fetcher_operator(
        "fetch_gw",
        generate_gw_fetcher_params,
        ["gw"],
    )
    gw_fetch_data_step.dag = dag
    gw_fetch_data_step.set_upstream(previous_step)

    gw_select_step = generate_cdo_select_operator(
        "select_gw",
        generate_gw_cdo_select_params,
        "gw",
    )
    gw_select_step.dag = dag

    gw_select_step.set_upstream(gw_fetch_data_step)

    # plot
    plot_step = generate_plotter_operator(
        "plot",
        generate_plotter_params,
    )
    plot_step.dag = dag

    plot_step.set_upstream(gw_select_step)
