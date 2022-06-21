import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Api-Test", 
    version="0.0.1",
    author="Priyam Bajpai",
    author_email="priyambajpai302@gmail.com",
    description="A package to test apis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/golubajpai/apitest3.6",
    packages=setuptools.find_packages(),
install_requires=[
   "attrs==19.3.0",
"certifi==2019.11.28",
"chardet==3.0.4",
"idna==2.8",
"importlib-metadata==1.1.0",
"more-itertools==8.0.0",
"numpy==1.22.0",
"packaging==19.2",
"pandas==0.25.3",
"pluggy==0.13.1",
"py==1.8.0",
"pyparsing==2.4.5",
"pytest==5.3.1",
"pytest-xdist==1.30.0",
"python-dateutil==2.8.1",
"pytz==2019.3",
"requests==2.22.0",
"six==1.13.0",
"urllib3==1.25.7",
"wcwidth==0.1.7",
"zipp==0.6.0"
],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

