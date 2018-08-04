import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="billionfong",
    version="1.2.4.1",
    author="Billy Fong",
    author_email="billionfong@billionfong.com",
    description="Welcome to billionfong's playground",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://www.billionfong.com/",
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
