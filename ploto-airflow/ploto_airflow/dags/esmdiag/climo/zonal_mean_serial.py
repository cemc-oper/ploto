# coding: utf-8
"""ESMDIAG's climo/zonal_mean figure workflow, serial version.

Warning
-------
This is a test workflow.

Example
-------
Run the following command to test:

   $ airflow trigger_dag \
     --conf "$(jq '.' ./common_example.json)" \
     ploto_esmdiag_climo_zonal_mean_serial

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
    generate_esmdiag_vinterp_processor_params,
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
from ploto_airflow.operators.processor.esmdiag_data_processor.vinterp import (
    generate_operator as generate_vinterp_operator
)

args = {
    "owner": "ploto",
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}

dag_id = "ploto_esmdiag_climo_zonal_mean_serial"

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
    previous_step = create_dir_step

    # fetch and process data
    fields = [
        'T',
        'U',
        'V',
        'Q',
        'PS'
    ]
    fetch_data_step = generate_edp_fetcher_operator(
        "fetch_data",
        generate_fetcher_params,
        fields,
    )

    fetch_data_step.dag = dag
    fetch_data_step.set_upstream(previous_step)
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

    # vinterp
    uvt_levels = [1000, 925, 850, 775, 700, 600, 500, 400,
                  300, 250, 200, 150, 100, 70, 50, 30, 10]
    q_levels = [1000, 925, 850, 775, 700, 600, 500, 400, 300]

    for field in ["U", "V", "T"]:
        vinterp_step = generate_vinterp_operator(
            f"vinterp_{field}",
            generate_esmdiag_vinterp_processor_params("gamil"),
            [{
                "var_name": field,
                "levels": uvt_levels,
                "interp_type": "linear",
                "extrap": "False"
            }],
        )
        vinterp_step.set_upstream(previous_step)
        previous_step = vinterp_step

    for field in ["Q"]:
        vinterp_step = generate_vinterp_operator(
            f"vinterp_{field}",
            generate_esmdiag_vinterp_processor_params("gamil"),
            [{
                "var_name": field,
                "levels": q_levels,
                "interp_type": "linear",
                "extrap": "False"
            }],
        )
        vinterp_step.set_upstream(previous_step)
        previous_step = vinterp_step

    # fetch and process gw
    gw_fetch_data_step = generate_edp_fetcher_operator(
        "fetch_gw",
        generate_gw_fetcher_params,
        ["gw"],
    )
    gw_fetch_data_step.dag = dag
    gw_fetch_data_step.set_upstream(previous_step)
    previous_step = gw_fetch_data_step

    gw_select_step = generate_cdo_select_operator(
        "select_gw",
        generate_gw_cdo_select_params,
        "gw",
    )
    gw_select_step.dag = dag
    gw_select_step.set_upstream(previous_step)
    previous_step = gw_select_step

    # plot
    plot_step = generate_plotter_operator(
        "plot",
        generate_plotter_params,
    )
    plot_step.dag = dag

    plot_step.set_upstream(previous_step)
