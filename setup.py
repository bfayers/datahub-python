from setuptools import find_packages, setup

setup(
    name="datahub",
    packages=find_packages(include=["datahub"]),
    version="0.5",
    description="MetOffice DataHub Library",
    author="bfayers",
    license="GPLv3",
    install_requires=["requests>=2.25.1"],
)
