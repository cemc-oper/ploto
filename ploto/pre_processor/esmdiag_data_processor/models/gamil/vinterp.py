# coding: utf-8
from pathlib import Path
import subprocess
import os
import sys
import json

from ploto.logger import get_logger


def run_task(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'esmdiag_data_processor',
            'action: 'vinterp',
            'model': 'gamil',
            'tasks': [
                {
                    "var_name": "U",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false"
                },

                {
                    "var_name": "V",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false"
                },
                {
                    "var_name": "Q",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300],
                    "interp_type": "linear",
                    "extrap": "False"
                },
                {
                    "var_name": "T",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "log",
                    "extrap": "False"
                }
            ],
            common: {
                model_info: {
                    id: "FGOALS-g3",
                    atm_id: "GAMIL",
                    ocn_id: "LICOM",
                    ice_id: "CICE",
                },
                case_info: {
                    id: "piControl-bugfix-licom-80368d",
                },
                date: {
                    start: "0030-01-01",
                    end: "0060-12-31"
                }
            },
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()

    model = task["model"]
    MODEL = model.upper()
    common_config = task["common"]
    vinterp_ncl_script = Path(Path(__file__).parent, "vinterp.ncl")

    for vinterp_task in task["tasks"]:
        var_name = vinterp_task["var_name"]
        var_file_pattern = "{model}.{case_id}.{name}.monthly.{start_date}:{end_date}.nc"
        ps_path = var_file_pattern.format(
            model=MODEL,
            case_id=common_config["case_info"]["id"],
            name="PS",
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        )
        var_path = var_file_pattern.format(
            model=MODEL,
            case_id=common_config["case_info"]["id"],
            name=var_name,
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        )
        levels = vinterp_task["levels"]

        interp_type = vinterp_task["interp_type"]
        if interp_type == "linear":
            interp_type = 1
        elif interp_type == "log":
            interp_type = 2
        else:
            logger.fatal("interp type is not supported:", interp_type)
            return False

        extrap = vinterp_task["extrap"]
        out_path = "{model}.{case_id}.{name}.monthly.vinterp{levels}.{start_date}:{end_date}.nc".format(
            model=MODEL,
            case_id=common_config["case_info"]["id"],
            name=var_name,
            levels=":".join([str(level) for level in levels]),
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        )

        esmdiag_env = os.environ.copy()
        esmdiag_env["ESMDIAG_ROOT"] = config["esmdiag"]["root"]

        logger.info("run vinterp.ncl for {var_name}...".format(var_name=var_name))
        ncl_result = subprocess.run(
            [
                '/bin/bash',
                '-i', '-c',
                'ncl '
                'ps_path=\\"{ps_path}\\" '
                'var_path=\\"{var_path}\\" '
                'var_name=\\"{var_name}\\" '
                'plevs=\\(/{plevs}/\\) '
                'interp_type={interp_type} '
                'extrap={extrap} '
                'out_path=\\"{out_path}\\" '
                '{ncl_script}'.format(
                    ps_path=ps_path,
                    var_path=var_path,
                    var_name=var_name,
                    plevs=",".join([str(level) for level in levels]),
                    interp_type=interp_type,
                    extrap=extrap,
                    out_path=out_path,
                    ncl_script=vinterp_ncl_script)
            ],
            env=esmdiag_env,
            start_new_session=True
        )

        logger.info("run vinterp.ncl for {var_name}...done".format(var_name=var_name))
    return True
