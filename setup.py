import os
from setuptools import find_packages, setup

with open('requirements.txt') as req_f:
    requirements = req_f.read().splitlines()

setup(name='Charactr API SDK',
  version='0.0.1',
  description='Python SDK to interact with the charactr API.',
  author='charactr',
  author_email='contact@charactr.com',
  url='https://github.com/charactr-platform/charactr-api-sdk-python',
  packages=find_packages(),
  include_package_data=True,
  install_requires=requirements,
  python_requires='>=3.7.0',
  setup_requires=[
    'setuptools==50.3.0'
  ]
)
