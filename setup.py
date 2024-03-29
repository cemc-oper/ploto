from setuptools import setup, find_packages
from codecs import open
from os import path
import io
import re


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with io.open("ploto/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


requires_all = [
    "loguru"
]


setup(
    name='ploto',

    version=version,

    description='A distributed scheduling platform for plotting system',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/nwpc-oper/ploto',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='Apache License, Version 2.0',

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={},

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        'pika',
        'requests',
    ],

    extras_require={
        'all': requires_all,
        'test': [],
        'gidat': [
            'cx_Oracle'
        ],
        'earth': [
            'celery',
            'netCDF4',
            'elasticsearch==6.3.1',
            'redis',
            'sqlalchemy',
        ]
    }
)