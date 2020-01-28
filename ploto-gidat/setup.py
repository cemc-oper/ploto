# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='ploto-gidat',

    version='0.2',

    description='Ploto-gidat project.',
    long_description=__doc__,

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ['*.ncl'],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        'pika',
        'requests',
        'sqlalchemy',
        'loguru',
        'cx_Oracle'
    ],

    extras_require={
        'test': [],
    }
)