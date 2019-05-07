# coding=utf-8
import importlib
from ploto_server.common.esmdiag import metrics


def generate_metric_tasks(metric_config, common_config) -> list:
    metric_name = metric_config["name"]
    try:
        metric_package = importlib.import_module("ploto_server.common.esmdiag.metrics.{metric}".format(metric=metric_name), metrics)
    except ImportError:
        print("metric {metric} not found".format(metric=metric_name))
        return list()

    tasks = metrics.generate_figure_tasks(
        metric_config=metric_config,
        common_config=common_config
    )

    return tasks
