from setuptools import setup

setup(
    name="cppState",
    version="1.0.0",
    install_requires=["pybind11"],
    ext_modules=[Extension("cppState", ["state.cpp", "state.hpp"])]
)
