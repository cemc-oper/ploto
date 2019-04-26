# coding=utf-8
from . import cat_file_pre_processor, empty_processor, esmdiag_data_processor, cdo_processor


pre_processor_map = {
    'cat_file_pre_processor': cat_file_pre_processor,
    'esmdiag_data_processor': esmdiag_data_processor,
    'cdo_processor': cdo_processor
}


def do_pre_processing(tasks, work_dir, config):
    for task in tasks:
        task_type = task['type']
        processor = pre_processor_map.get(task_type, empty_processor)
        processor.run_pre_processor(task, work_dir, config)
