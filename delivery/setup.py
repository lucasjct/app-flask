from setuptools import setup, find_packages

setup(
    name="delivery",
    version="0.1.0", #major, minor, patch
    description="Delivery app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"]
)