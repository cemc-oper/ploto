# coding: utf-8
import importlib

from ploto.logger import get_logger


def run_plotter(plotter_config, work_dir, config) -> bool:
    """

    :param plotter_config:
        {
            metric: 'climo',
            figure: 'precip',
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
        {
            'esmdiag': {
                'root': root dir
            }
        }
    :return:
    """
    logger = get_logger()
    metric = plotter_config["metric"]
    from ploto.plotter import esmdiag_plotter
    try:
        metric_module = importlib.import_module(
            "ploto.plotter.esmdiag_plotter.metrics.{metric}".format(metric=metric))
    except ImportError:
        logger.error("can't found metric {metric}".format(metric=metric))
        return False
    metric_module.run_task(plotter_config, work_dir, config)
    return True
