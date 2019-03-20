# coding: utf-8
import os


def test_cat_file_pre_processor():
    task = {
        'type': 'cat_file_pre_processor',
        'file_list': [
            '1.txt',
            '2.txt',
            '3.txt'
        ],
        'target': 'sum.txt'
    }

    os.chdir("/space/windroc/workspace/plot/playground/cat_file_playground")
    from ploto.pre_processor.cat_file_pre_processor import run_pre_processor
    print("run test...")
    run_pre_processor(task, os.getcwd(), {})
    print("run test...Done")


test_cat_file_pre_processor()
