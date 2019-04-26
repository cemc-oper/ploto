# coding=utf-8
from ploto.processor import (
    cat_file_processor,
    cdo_processor,
    copy_file_processor,
    empty_processor,
    esmdiag_data_processor,
    gidat_post_processor
)

processor_map = {
    'cat_file_processor': cat_file_processor,
    'cdo_processor': cdo_processor,
    'copy_file_processor': copy_file_processor,
    'empty_processor': empty_processor,
    'esmdiag_data_processor': esmdiag_data_processor,
    'gidat_post_processor': gidat_post_processor,
}


def do_processing(tasks, work_dir, config):
    for task in tasks:
        task_type = task['type']
        processor = processor_map.get(task_type, empty_processor)
        processor.run_processor(task, work_dir, config)
