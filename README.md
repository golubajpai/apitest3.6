

1. use package by setup.py 
1.1 install virtualenv  and activate them then run setup.py install 
# ApiTestGenerics

pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options

pytest -n=(no. of threads)= you can run multiple apis
pytest -v = to run the pytest command


################################--Run test_api.py ---###################


1.for testing you have to run test_api.py file.

2.if base encoding is required then call apicall() method 

2.if base64 encoding is not required then call api() method after the creation of constructor.