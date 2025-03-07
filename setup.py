from setuptools import setup, find_packages

setup(
    name="richpride",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich",  # This is a dependency on the Rich module
    ],
    author="Safey",
    author_email="bytesarecool@gmail.com",
    description="A collection of pride flag emojis for the rich module",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SafeyX3/richpride",  # Replace with your actual URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
