from setuptools import setup, find_packages

setup(
    name="electricity_fraud_prediction",
    version="0.1.0",
    author="Franck KD",
    description="A machine learning pipeline for predicting electricity fraud based on meter data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FranckKD/electricity-fraud-prediction",
    packages=find_packages(exclude=["tests", "notebooks"]),
    install_requires=[
        "pandas>=1.3",
        "numpy>=1.21",
        "scikit-learn>=1.0",
        "xgboost>=1.5",
        "pyyaml>=6.0",
        "pytest>=7.0",
        "matplotlib>=3.4",
        "seaborn>=0.11",
        "jupyterlab>=3.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.7',
)