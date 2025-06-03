from setuptools import setup, find_packages

setup(
    name="smoothcolors",  
    version="0.1.0",
    author="Wock 2009",
    description="A python package for clean smooth colors for your CLI terminal tools!",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://coderhangout.xyz",
    packages=find_packages(), 
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    keywords="terminal colors gradient text cli",
    license="MIT",
    project_urls={
        "Homepage": "https://coderhangout.xyz",
    },
)
