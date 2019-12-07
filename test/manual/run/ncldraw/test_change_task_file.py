# coding=utf-8
import os
import warnings
from xml.etree import cElementTree

# from ploto.plotter.ncldraw_plotter import change_task_file


def test_change_task_file():
    warnings.warn("this test is not completed", Warning)
    task_file_path = os.path.join(os.path.dirname(__file__), 'task.xml')
    tree = cElementTree.parse(task_file_path)
    root = tree.getroot()

    node = root.find(".//task/workstation")

    print(node)


if __name__ == "__main__":
    test_change_task_file()
