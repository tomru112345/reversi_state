from setuptools import setup


ext_modules = [
    Extension(
        'cppState',  # ライブラリ名
        ['src/statebind.cpp'],  # 参照にするファイル
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            get_pybind_include(user=True)
        ],
        language='c++'
    ),
]

setup(
    name='cppState',  # ライブラリ名
    version=0.1,
    author='tamura kazuma',
    description='state written by cpp',
    long_description='',
    ext_modules=ext_modules,
    install_requires=['pybind11>=2.10'],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)
