#!/usr/bin/env python3
import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'helloworldpython3/HelloWorldPython3.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="HelloWorldPython3",
    version=__version__,
    description="Dummy test for Python3",
    py_modules=['helloworldpython3.HelloWorldPython3'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
