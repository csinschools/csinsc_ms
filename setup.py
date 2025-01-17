import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csinsc-ms",
    version="1.1.0.6",
    author="Toan Huynh",
    author_email="toan@csinschools.com",
    description="Tools and libraries used in the CS in Schools programme.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csinschools/csinsc-ms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
