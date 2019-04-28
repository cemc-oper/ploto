# coding=utf-8
from ploto.processor import (
    cat_file_processor,
    cdo_processor,
    copy_file_processor,
    esmdiag_data_processor,
    gidat_post_processor
)
from ploto.logger import get_logger

processor_map = {
    'cat_file_processor': cat_file_processor,
    'cdo_processor': cdo_processor,
    'copy_file_processor': copy_file_processor,
    'esmdiag_data_processor': esmdiag_data_processor,
    'gidat_post_processor': gidat_post_processor,
}


logger = get_logger()


def do_processing(tasks, work_dir, config):
    for task in tasks:
        task_type = task['type']
        processor = processor_map.get(task_type, None)
        if processor is None:
            logger.warn("processor type not supported: {type}".format(type=task['type']))
            return
        processor.run_processor(task, work_dir, config)
