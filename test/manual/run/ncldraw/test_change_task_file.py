# coding=utf-8
import os
import xml.etree.cElementTree as ET

from ploto.plotter.ncldraw_plotter.ncldraw_util import change_task_file


def main():
    task_file_path = os.path.join(os.path.dirname(__file__), 'task.xml')
    tree = ET.parse(task_file_path)
    root = tree.getroot()

    node = root.find(".//task/workstation")

    print(node)


if __name__ == "__main__":
    main()
