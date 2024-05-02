from setuptools import setup, find_packages

setup(
    name='Pyskey',
    version='0.0.1',
    packages=find_packages(),
    author='nennneko5787',
    author_email='nennneko5787@14chan.jp',
    description='A python wrapper library for misskey!',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nennneko5787/Pyskey',
    install_requires=[
        'aiohttp',
    ],
    license='GPL-3.0-only',
    python_requires='>=3.10',
)
