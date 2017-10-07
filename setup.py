# coding=utf-8
"""Python pro1AC setup script."""
from setuptools import setup

setup(
    name='pro1AC',
    packages=['pro1AC'],
    version='0.0.1',
    description='Python Library for PRO1 Thermostat',
    author='Ryan Viernes',
    author_email='ryanviernes@gmail.com',
    url='https://github.com/ryanfriday/pro1AC',
    license='LGPLv3+',
    include_package_data=True,
    install_requires=['requests', 'pytz'],
    test_suite='tests',
    keywords=[
        'thermostat',
        'pro1ac',
        'home automation',
        ],
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' +
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)