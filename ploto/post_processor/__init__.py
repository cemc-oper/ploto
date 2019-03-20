# coding=utf-8
from ploto.post_processor import copy_file_post_processor, empty_post_processor


post_processor_map = {
    'copy_file_post_processor': copy_file_post_processor
}


def do_post_processing(tasks, work_dir, config):
    for task in tasks:
        task_type = task['type']
        processor = post_processor_map.get(task_type, empty_post_processor)
        processor.run_post_processor(task, work_dir, config)
