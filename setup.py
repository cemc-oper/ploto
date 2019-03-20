# coding=utf-8
from setuptools import setup

setup(
    name='ploto',

    version='0.1',

    description='GIDAT plot.',
    long_description=__doc__,

    packages=[
        'ploto',
        'ploto_server'
    ],

    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        'pika',
        'flask',
        'sqlalchemy',
        'cx_Oracle'
    ]
)