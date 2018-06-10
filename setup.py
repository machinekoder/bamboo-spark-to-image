# coding=utf-8
from setuptools import setup

setup(
    name='bamboo-spark-to-image',
    version='1.0',
    package_dir={'': 'src'},
    packages=['bamboo_spark_to_image'],
    url='https://github.com/machinekoder/bamboo-spark-to-image',
    license='MIT',
    author='Alexander Rössler',
    author_email='alex@machinekoder.com',
    description='Converts Bamboo Spark generated PDF to images',
    install_requires=['sh'],
    scripts=['bin/bamboo_spark_to_image'],
)
