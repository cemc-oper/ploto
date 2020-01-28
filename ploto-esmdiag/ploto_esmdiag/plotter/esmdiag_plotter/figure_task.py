# coding: utf-8
import os
import subprocess

from ploto.logger import get_logger


def draw_figures(ncl_script, task, work_dir, config):
    """

    :param ncl_script:
    :param task:
        {
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
    os.chdir(work_dir)
    common_config = task["common"]

    esmdiag_env = os.environ.copy()
    esmdiag_env["ESMDIAG_ROOT"] = config["esmdiag"]["root"]
    # logger.info(esmdiag_env)

    logger.info("run ncl script...")
    ncl_command = [
        # '/bin/bash',
        # '-i', '-c',
        'ncl -Q '
        'model_id=\\"{model_id}\\" '
        'model_atm_id=\\"{model_atm_id}\\" '
        'model_ocn_id=\\"{model_ocn_id}\\" '
        'model_ice_id=\\"{model_ice_id}\\" '
        'case_id=\\"{case_id}\\" '
        'start_date=\\"{start_date}\\" '
        'end_date=\\"{end_date}\\" '
        '{ncl_script}'.format(
            model_id=common_config["model_info"]["id"],
            model_atm_id=common_config["model_info"]["atm_id"],
            model_ocn_id=common_config["model_info"]["ocn_id"],
            model_ice_id=common_config["model_info"]["ice_id"],
            case_id=common_config["case_info"]["id"],
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
            ncl_script=ncl_script)
    ]
    logger.info("ncl command: {ncl_command}".format(ncl_command=' '.join(ncl_command)))
    ncl_result = subprocess.run(
        ncl_command,
        env=esmdiag_env,
        # start_new_session=True,
        shell=True,
    )
    logger.info("run ncl script...done")

