# Python Tech Challenge  

---
## 1 - The Problem  

- The challenge is to create a program that computes some  
basic statistics on a collection of small positive integers. You  
can assume all values will be less than 1,000.  
- Implement this challenge in whatever programming language  
best highlights your skills. Also, please supply a README with  
details on how to setup and run your application.

### Requirements

The **DataCapture** object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.
Here’s the program skeleton in Python to explain the structure:
```python
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only values greater than 4)
```

### Challenge conditions:
- You cannot import a library that solves it instantly
- The methods add(), less(), greater(), and between() should have constant time O(1)
- The method build_stats() can be at most linear O(n)
- Apply the best practices you know
- Share a public repo with your project

### PLEASE FOLLOW THE INSTRUCTIONS
- Technical challenge should be completed within the next 3 days.
- Tests must be included in the submission.
- Do not split error input validation between the command line code and the class methods, this is not something considered as a best practice.
- Do not create a driver script via the command line, it is not necessary, we are only seeking working classes and tests, as we can run the program via the Python repl.
- Please apply any best practice you think will add value, but do not add extra feature than the requested.
- Please upload the solution to a repository and share the link to recruiting_CO@teaminternational.com
- If you have questions or inconveniences to complete the test, don’t hesitate to ask your recruiter
---
## 2 - The Solution

The *DataCapture* Class is divided in two subclasses: *Capture* and *Stats*. The first one is responsible for create the list of numbers and the other is responsible the required statistics creation. The second class is direct callable but Capture class create a object for this classe for you:

### Example of use

```
Python 3.9.10 (main, Mar  9 2022, 20:59:48)    
Type 'copyright', 'credits' or 'license' for more information  
IPython 8.18.1 -- An enhanced Interactive Python. Type '?' for help.  
  
In [1]: from src.DataCapture.capture import Capture  
  
In [2]: from random import randint  
  
In [3]: x = [randint(0,1000) for i in range(1000000)]  
  
In [4]: cap = Capture()  
  
In [5]: for i in x:  
  ...:     cap.add(i)  
  ...:    
  
In [6]: stats = cap.build_stats()  
  
In [7]: stats.less(100)  
Out[7]: 100102  
  
In [8]: stats.greater(700)  
Out[8]: 299326  
  
In [9]: stats.between(500, 600)  
Out[9]: 100164  
  
In [10]:
```

### Dependencies

The project don't have real dependencies besides the Python version (must be superior to 3.5 because of the type hints). The above exemplo can be realised in regular Cpython.

The project provides a series of elementar tests for the class methods. To make use of then is recommended to use the Poetry for create virtual environment 

#### Example
```
╭─    ~/zSource/Python/xxx  
╰─ poetry install 

Creating virtualenv indigo-9JbxvFb1-py3.9 in /home/master/.cache/pypoetry/virtualenvs  
Installing dependencies from lock file  
  
Package operations: 26 installs, 0 updates, 0 removals  
  
 • Installing six (1.16.0)  
 • Installing asttokens (2.4.1)  
 • Installing executing (2.0.1)  
 • Installing parso (0.8.3)  
 • Installing ptyprocess (0.7.0)  
 • Installing pure-eval (0.2.2)  
 • Installing traitlets (5.14.0)  
 • Installing wcwidth (0.2.12)  
 • Installing decorator (5.1.1)  
 • Installing exceptiongroup (1.2.0)  
 • Installing iniconfig (2.0.0)  
 • Installing jedi (0.19.1)  
 • Installing matplotlib-inline (0.1.6)  
 • Installing nodeenv (1.8.0)  
 • Installing packaging (23.2)  
 • Installing pexpect (4.9.0)  
 • Installing pluggy (1.3.0)  
 • Installing prompt-toolkit (3.0.42)  
 • Installing pygments (2.17.2)  
 • Installing stack-data (0.6.3)  
 • Installing tomli (2.0.1)  
 • Installing typing-extensions (4.9.0)  
 • Installing ipython (8.18.1)  
 • Installing pyright (1.1.339)  
 • Installing pytest (7.4.3)  
 • Installing ruff (0.1.7)  
╭─    ~/zSource/Python/xxx 
╰─ poetry shell 
Spawning shell within ~/.cache/pypoetry/virtualenvs/indigo-9JbxvFb1-py3.9  
~/.cache/pypoetry/virtualenvs/indigo-9JbxvFb1-py3.9/bin/activate 
╭─    ~/zSource/Python/xxx  ✔  indigo-9JbxvFb1-py3.9 🐍    
╰─ pytest 
================================================================================= test session starts =================================================================================
platform linux -- Python 3.9.10, pytest-7.4.3, pluggy-1.3.0  
rootdir: /home/master/zSource/Python/xxx  
collected 8 items   
tests/test_capture.py ....                                                                     [ 50%]  
tests/test_stats.py ....                                                                     [100%]  
  
================================================================================= 8 passed in 0.03s =================================================================================
```


Commands:
```
poetry install
poetry shell
pytest
```

**Obs**: If poetry is not present, you can have all the instructions for the different forms of instalation  in the official page of the program:

[Poetry/](https://python-poetry.org)

The most common form is:
```
pip install poetry

ou

pipx install poetry
```
The last one is more recomended