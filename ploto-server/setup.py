# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='ploto-server',

    version='0.2',

    description='Ploto server.',
    long_description=__doc__,

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        'flask',
        'requests'
    ],

    extras_require={
        'test': [],
    }
)