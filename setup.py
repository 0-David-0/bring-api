import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BringApi",
    version="0.0.1",
    author="Philipp Dürr",
    author_email="phil@uselessbrickwall.com",
    description="Unofficial Bring! Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philipp2310/bring-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)