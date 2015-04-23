from setuptools import setup, find_packages

setup(
    name='datapopserv',
    version='0.1',
    url='',
    license='',
    packages=find_packages(),
    author='mikhail91',
    author_email='mikhail91@yandex-team.ru',
    description='Api service for DataPopularity module',
    install_requires=[
        'flask == 0.10.1',
        'flask-restful == 0.3.2',
        'Werkzeug == 0.10.1',
        'rep==0.5.0',
        'datapop==0.2'
    ],
)
