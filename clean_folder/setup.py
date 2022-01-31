import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean_folder",
    version="0.0.1",
    author="dontbelikeme",
    author_email="blw1@rambler.ru",
    description="A simple file-sorter",
    entry_points={
        'console_scripts': [
            'clean_folder = clean_folder.clean',
        ],
    },
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/dontbelikeme/GoIt_python_hw_7.git",
    project_urls={
        "Bug Tracker": "https://github.com/ontbelikeme/",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)