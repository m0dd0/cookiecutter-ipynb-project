import setuptools

setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    # description="",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="",
    classifiers=["Programming Language :: Python :: 3"],
    packages=setuptools.find_packages(),
    python_requires="==3.10",
    # not specifying versions might result in pip downloading multiple versions
    # of a package in order to solve dependencies
    # therfore it might be useful to fix the versions someday
    install_requires=[
        "jupyter",
        "numpy",
        "nptyping",
        "matplotlib",
    ],
    extras_require={"dev": ["black", "pylint"]},
    include_package_data=True,
    use_scm_version=True,
)