from setuptools import setup, find_packages

setup(
    name='Pyskey',
    version='0.0.1',
    packages=find_packages(),  # 自動的にパッケージを検索して追加します
    author='nennneko5787',
    author_email='nennneko5787@14chan.jp',
    description='A python rapper library for misskey!',
    long_description=open('README.md').read(),  # README.mdファイルの内容を使用します
    long_description_content_type='text/markdown',
    url='https://github.com/nennneko5787/Pyskey',
    install_requires=[  # パッケージの依存関係をリストします
        'aiohttp',
    ],
    license='GPL-3.0-only',  # ライセンスを指定
    python_requires='>=3.10',
)
