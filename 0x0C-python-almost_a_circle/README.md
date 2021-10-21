#### 0x0C-python-almost_a_circle       
================================       
The directory contains projects on the most python objects such as class and inheritance.    
After each test, a unnitest is created for individual functions and classes.      

**Concepts**   
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)     
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)     
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)     

**Task 0: Test Range**    

* Creating a range of tests for the functions.    
* All the tests starts with `test_`   
* File organization in the test is similar to project e.g `models/base.py` is tested by `tests/test_models/test_base.py`    
* tests are executed by the command `python3 -m unittest discover tests`    
* Individual tests are executed by the command `python3 -m unittest tests/test_models/test_base.py`     

**Task 1: Base Class**     

* This is the first class upon which other classes would inherit.    
* A new folder `models` is created with an empty file `__init__.py` which makes the folder becomes a python package.      
* A class constructor is created and private class attribute `__nb_objects` is also created. 
