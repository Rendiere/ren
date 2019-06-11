from setuptools import find_packages, setup

setup(
    name='ren',
    packages=find_packages(),
    version='0.1.0',
    description='Personal data science utilities library',
    author='Renier Botha',
    python_required=">3.6.0",
    install_requires=[
        'scipy',
        'pandas',
        'numpy',
        'sklearn',
        'matplotlib',
        'xgboost',
        'lightgbm',
        'catboost',
    ]
)