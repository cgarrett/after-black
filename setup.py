from setuptools import find_packages
from setuptools import setup

setup(
    name="after_black",
    description="To help idenitfy possible formatting issues after running the Black formatter.",
    url="https://github.com/cgarrett/after-black",
    version="v0.0.1",

    author="Chris Garrett",
    author_email="christopher.garrett@austin.utexas.edu",

    classifiers=[
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages("./src"),
    entry_points={
        "console_scripts": [
            "after_black=src.after_black:main",
        ],
    },
)
