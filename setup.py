from setuptools import find_packages, setup


with open('requirements.txt') as req_f:
    requirements = req_f.read().splitlines()

setup(name='charactr_api',
      description='Python SDK to interact with the charactr API.',
      long_description=open('README.md').read(),
      version='1.0.0',
      author='charactr',
      author_email='contact@charactr.com',
      url='https://github.com/charactr-platform/charactr-api-sdk-python',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.8.0',
      setup_requires=[
        'setuptools==58.0.4'
      ]
      )
