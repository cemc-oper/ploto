# coding: utf-8
import importlib


def generate_figure_tasks(metric_config, common_config) -> list:
    metric_name = metric_config['name']
    figures = metric_config["figures"]
    tasks = list()

    for figure_config in figures:
        figure_name = figure_config["name"]
        try:
            figure_module = importlib.import_module(
                "ploto_server.common.esmdiag.metrics.{metric}.figures.{figure}".format(
                    metric=metric_name,
                    figure=figure_name))
        except ImportError:
            print("figure not found: {figure}".format(figure=figure_name))
            continue
        task = figure_module.generate_figure_task(figure_config, common_config)
        tasks.append(task)

    return tasks
