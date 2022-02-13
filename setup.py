import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean_folder",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean:main'
        ]
    },
    python_requires=">=3",
)