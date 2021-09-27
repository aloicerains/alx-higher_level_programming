#### Directory 0x05-python-exceptions  
The directory contains programs and files dealing with error and exception handling in python.  
Some of the files present include:  
- [x] **0-safe_print_list.py**  
Function prints x elements of a list
* Prototype: `def safe_print_list(my_list=[], x=0):`  
* my_list can contain any type (integer, string, etc.)  
* All elements must be printed on the same line followed by a new line.  
	x represents the number of elements to print  
	x can be bigger than the length of my_list
* Returns the real number of elements printed  
* You have to use try: / except   
- [x] **1-safe_print_integer.py**  
Function prints an integer with "{:d}".format().  
value can be any type such as string and integers.  
Returns: `True` if value is correctly printed, otherwise `False`  
- [x] **2-safe_print_list_integers.py**
* Function prints integer elements in a list   
* It escapes the non integer elements  
* Function returns the number of integers printed   
- [] **3-safe_print_division.py**   
* Function divides two integers and prints the result   
* Return the result   
* The result of dividion are printed in the finally section   
- [] **4-list_division.py**   
* Function divides the list 1 by list 2   
* Returns a new list of size list_lenth given as function argument   
* ZeroDivision, Index, and Type erros are handled    
- [] **5-raise_exception.py***   
Function raises `TypeError'   
- [x] **6-raise_exception_msg.py**   
Function raises `NameError` with an error message   
- [x] **100-safe_print_integer_err.py**   
Function prints an integer followed by a newline.   
* Returns `True` if value is integer   
* Returns `False` if value is not integer and writes in stdout the Error message    
- [x] **101-safe_function.py**   
Function executes a function safely      
Function prototype: `def safe_function(fct, *args)`    
* Assume `fct` will always be a pointer   
* Return the result of the function   
* Otherwise returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`    
* Uses `try: / except`   

