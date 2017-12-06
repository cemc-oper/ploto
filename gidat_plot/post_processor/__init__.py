# coding=utf-8
from gidat_plot.post_processor import copy_file_post_processor
from gidat_plot.logger import get_logger


def run_post_processor(task, work_dir, config):
    logger = get_logger()
    logger.info("task type not supported:", task['type'])


post_processor_map = {
    'copy_file_post_processor': copy_file_post_processor
}


def do_post_processing(tasks, work_dir, config):
    for task in tasks:
        task_type = task['type']
        processor = post_processor_map.get(task_type, do_post_processing.__module__)
        processor.run_post_processor(task, work_dir, config)
