# coding=utf-8
from setuptools import setup

setup(
    name='gidat-plot',

    version='0.1',

    description='GIDAT plot.',
    long_description=__doc__,

    packages=[
        'gidat_plot',
        'gidat_server'
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