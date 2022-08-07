from setuptools import find_namespace_packages, setup
from setuptools_rust import RustExtension

setup(
    name="rulec",
    version="0.1.0",
    packages=find_namespace_packages(
        include=["rulec", "rulec.*"],
    ),
    setup_requires=["setuptools", "setuptools_rust"],
    zip_safe=False,
    rust_extensions=[
        RustExtension("rulec.rust")
    ],
    include_package_data=True,
)
