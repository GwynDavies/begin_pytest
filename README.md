# Overview

This is a Python project to demonstrate, how you can set up and get started, testing 
with Pytest:
- https://docs.pytest.org/

The project implements the "Little Man Computer", as described on the following
wiki page:
- see https://en.wikipedia.org/wiki/Little_man_computer

---

# Associated YouTube videos

For the associated YouTube videos, see the following playlist:
- https://www.youtube.com/playlist?list=PLZ4UK6jesoMdJ3SRiS5ISgFh-tYCnSf0M

---

# Requirements

## Experience

### Python
You will need to have some basic experience with Python programming

You will also need to have Python **3.7+** installed. The version can be checked
by using the -V argument with your Python installation:

```commandline
python -V
```

### Command line

You will also need a basic familiarity with the commandline of your computer, as the 
project and its usage are command line based

---

# Setup 

If your python executable is python

## Create a virtual environment

Create a python virtual environment, also use **"venv"** for the environment name, 
in order to use the included set-up scripts to work:

```commandline
python -m venv venv
```

## Activate the virtual environment

Window DOS:
```
.\set_venv_and_pythonpath.bat
```

Windows Powershell:
```
.\set_venv_and_pythonpath.ps1
```

Linux Bash (note the 2 .'s):
```
. ./set_venv_and_pythonpath.sh
```


##  Install required Python packages

With the virtual environment activated, use pip to install the following packages:

```commandline
pip install pytest
pip install pytest-cov
pip install pylint
pip install pylint-pytest
pip install autopep8
pip install pdoc
```


## Package information

- pytest  
  - https://docs.pytest.org/  
  - https://pypi.org/project/pytest/

- pytest-cov  
  - https://pypi.org/project/pytest-cov/  

- pylint  
  - https://pypi.org/project/pylint/  
  - https://pypi.org/project/pytest-pylint/  

- autopep8  
  - https://pypi.org/project/autopep8/  

- pdoc  
  - https://pypi.org/project/pdoc/  


---

# Running the example "Little man Computer" example code

Make sure the virtual environment is activated

```commandline
cd bin

python runme.py
```

---

# Running the associated pytest tests

Make sure the virtual environment is activated

Run pytest, pylint, autopep8 and pdoc:

```commandline
cd build

python ./build.py
```

If you just want to run pytest:

```commandline
cd build

python ./build.py test
```

To see the help listing:

```commandline
cd build

python ./build.py help

.****************************************************************************************************************.
'                                                                                                                 '
| Unable to process command line :                                                                                |
|                                                                                                                 |
| USAGE:     build.py               ... run all below                                                             |
|            build.py  test         ... run pytest                                                                |
|            build.py  lint         ... run pylint                                                                |
|            build.py  format       ... run autopep8                                                              |
|            build.py  docs         ... run pdoc                                                                  |
|                                                                                                                 |
| Received:  ./build.py help                                                                                      |
.                                                                                                                 .
'****************************************************************************************************************'

```