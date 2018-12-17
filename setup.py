"""Setup module for flaque project"""

from setuptools import setup, find_packages

TEST_REQ = ['pytest']
EXTRAS_REQ = {'test': TEST_REQ}

setup(
    name='flaque',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    setup_require=[
        'pytest-runner'
    ],
    install_requires=[
        'click',
    ],
    test_require=TEST_REQ,
    extra_require=EXTRAS_REQ,
    entry_points='''
        [console_scripts]
        flaque=flaque.__main__:main
    ''',
)
