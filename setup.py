import os
from setuptools import setup

with open(os.path.join('README.md')) as desc:
    LONG_DESCRIPTION = desc.read()

with open(os.path.join('requirements.txt')) as reqs:
    REQUIREMENTS = reqs.readlines()

setup(
    name='cytrader-binance',
    version='1.0.0',
    description='Binance API integration with cytrader',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/lindomar-oliveira/cytrader-binance',
    author='Saran Connolly',
    author_email='saran.c@pwecapital.com',
    license='MIT',
    packages=['cytrader_binance'],
    python_requires='>=3.7',
    keywords='cytrader,binance,bitcoin,bot,crypto,trading',
    install_requires=REQUIREMENTS
)
