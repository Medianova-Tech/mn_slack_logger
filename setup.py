from setuptools import setup, find_packages

setup(
    name='mn_slack_logger',
    description='Send FastAPI logs to Slack',
    version='0.0.1',
    author='Medianova',
    keywords=['python', 'slack logger', 'medianova'],
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    )
