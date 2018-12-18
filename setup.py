"""Setup module for flaque project"""

from setuptools import setup, find_packages

TEST_REQ = ['pytest']

setup(
    name='flaque',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'click',
    ],
    tests_require=TEST_REQ,
    entry_points='''
        [console_scripts]
        flaque=flaque.__main__:main
    ''',
)
