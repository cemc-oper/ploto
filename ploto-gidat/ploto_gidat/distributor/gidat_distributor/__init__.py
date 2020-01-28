# coding=utf-8
"""
Copy files to other location during post processing.

task schema:
    {
        "step_type": "distributor",
        'type': 'ploto.distributor.gidat_distributor',
        'plot_id': '', # plot_id,
        'plot_set_id': '', # plot_set_id
    }
"""
from sqlalchemy import create_engine


def run_distributor(task: dict, work_dir, config):
    processor_config = config['gidat_post_processor']
    database_config = processor_config['database']
    engine = create_engine(f'oracle+cx_oracle://{database_config["user"]}:{database_config["password"]}'
                           f'@{database_config["host"]}:{database_config["port"]}/{database_config["database_name"]}')
    conn = engine.connect()

    plot_id = task['plot_id']
    plot_set_id = task['plot_set_id']

    # update plot file status
    sql_string = f"UPDATE T_R_MET_PLOT_FILE SET STATUS='0' WHERE PLOT_FILE_ID='{plot_id}'"
    result = conn.execute(sql_string)
    print(result.rowcount)

    # TODO: update plot set status
