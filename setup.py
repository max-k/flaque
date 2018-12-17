from setuptools import setup, find_packages

with open('requirements-test.txt') as test_require:
    TEST_REQUIREMENTS = test_require.readlines()

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
    test_require=[
        TEST_REQUIREMENTS
    ],
    entry_points='''
        [console_scripts]
        flaque=flaque.__main__:main
    ''',
)
