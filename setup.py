from setuptools import find_packages, setup


with open("requirements.txt") as req_f:
    requirements = req_f.read().splitlines()

setup(
    name="charactr_api_sdk",
    description="Python SDK to interact with the charactr API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="2.0.1",
    author="charactr",
    author_email="support@gemelo.ai",
    url="https://github.com/charactr-platform/charactr-api-sdk-python",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.9.0",
    setup_requires=["setuptools==58.0.4"],
)
