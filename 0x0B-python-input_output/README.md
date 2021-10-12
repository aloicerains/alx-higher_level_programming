#### 0x0B-python-input_output    
=============================
This directory contains project files on how to handle input and ouput in python.    
The following tasks are present in the directory.     

- [x] **0-read_file.py**    

A function that reads a text file (UTF*) and prints it to stdout   
* Prototype: `def read_file(filename=""i):`    
* You must use the with statement     
* You don’t need to manage file permission or file doesn't exist exceptions.    
* You are not allowed to import any module     

- [x] **1-write_file.py**    

Function that writes a string to a text file and returns the number of characters written    
* Prototype: `def write_file(filename="", text=""):`    
* You must use the with statement    
* You don’t need to manage file permission exceptions.     
* Your function should create the file if doesn’t exist.    
* Your function should overwrite the content of the file if it already exists.    
* You are not allowed to import any module    

- [ ] **2-append_write.py**     

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:    
* Prototype: `def append_write(filename="", text=""):`      
* If the file doesn’t exist, it should be created     
* You must use the with statement    
* You don’t need to manage file permission or file doesn't exist exceptions.    
* You are not allowed to import any module