# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='ploto',

    version='0.2',

    description='Ploto project.',
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
    ],

    extras_require={
        'test': [],
        'gidat': [
            'cx_Oracle'
        ],
        'earth': [
            'celery',
            'netCDF4',
            'elasticsearch==6.3.1',
            'redis'
        ]
    }
)