***1. What is Python?***
- High-level  
- Interpreted  
- Object Oriented  
- Dynamically typed - no need to specify datatype for every variable  
- Scripting Language
**Special Features:**  
- Readability/ Syntactical Flexibility  
- Compatible with Windows, Linux, Mac etc.  

***3. What is the difference between lists and tuples?***
**List:**  
1. Lists are mutable  
2. Lists are slower  
3. Syntactical difference - use of square bracket
4. List offers no. of built-in functions
*What are built-in functions offered by Lists?*
    1.	list.append(obj) - Appends object obj to list
    2.	list.count(obj) - Returns count of how many times obj occurs in list
    3.	list.extend(seq) - Appends the contents of seq to list
    4.	list.index(obj) - Returns the lowest index in list that obj appears
    5.	list.insert(index, obj) - Inserts object obj into list at offset index
    6.	list.pop(obj=list[-1]) - Removes and returns last object or obj from list
    7.	list.remove(obj) - Removes object obj from list
    8.	list.reverse() - Reverses objects of list in place
    9.	list.sort([func]) - Sorts objects of list, use compare func if given

**Tuple:**  
1. Tuples are immutable  
2. Tuples are faster than tuples  
3. Syntactical difference - use of round bracket
4. Tuples do not offer built-in functions
*Why tuples are faster than lists?*  
Tuples are immutable, because:
    - Tuples are stored in a single continuous memory block
    - Thus, reallocation is never an issue which can cause slowness, like lists.
    - Therefore, tuples can be passed by reference directly once stored (as there is no modification ever)
    - Also, tuples don't have to utilise copies at every iteration unlike lists, which makes it faster

***4. What is pep 8?***
PEP in Python stands for Python Enhancement Proposal.It is a set of rules that specify how to write and design Python code for maximum readability.  
[Guidelines](https://www.python.org/dev/peps/pep-0008/)

***6. How is Memory managed in Python?***
- Memory in Python is managed by **Python private heap space**. All Python objects and data structures are located in a private heap. This private heap is taken care of by Python Interpreter itself, and a programmer doesn’t have access to this private heap.
- Python memory manager takes care of the allocation of Python private heap space.
- Memory for Python private heap space is made available by Python’s in-built garbage collector, which recycles and frees up all the unused memory.

***7. What is PYTHONPATH?***
- PYTHONPATH has a role similar to PATH. This variable tells Python Interpreter where to locate the module files imported into a program. - It should include the Python source library directory and the directories containing Python source code. 
- PYTHONPATH is sometimes preset by Python Installer.

***8. What are Python Modules?***
Files containing Python codes are referred to as Python Modules.
- This code can either be classes, functions or variables and saves the programmer time by providing the predefined functionalities when needed. 
- It is a file with .py extension containing an executable code.
- Commonly used built modules are listed below:
    - os
    - sys
    - data time
    - math
    - random
    - JSON

***9. What are python namespaces?***
**A Python namespace ensures that object names in a program are unique and can be used without any conflict.**   
Python implements these namespaces as dictionaries with ‘name as key’ mapped to its respective ‘object as value’.  
Some examples of namespaces:  
    - **Local Namespace** consists of local names inside a function. It is temporarily created for a function call and gets cleared once the function returns.
    - **Global Namespace** consists of names from various imported modules/packages that are being used in the ongoing project. It is created once the package is imported into the script and survives till the execution of the script.
    - **Built-in Namespace** consists of built-in functions of core Python and dedicated built-in names for various types of exceptions.

***11. What is scope resolution?***
**A scope is a block of code where an object in Python remains relevant.**
- Each and every object of python functions within its respective scope. 
- As Namespaces uniquely identify all the objects inside a program but these namespaces also have a scope defined for them where you could use their objects without any prefix. 
- Let’s have a look on scope created as the time of code execution:
    - A **local scope** refers to the local objects included in the current function.
    - A **global scope** refers to the objects that are available throughout execution of the code.
    - A **module-level scope** refers to the global objects that are associated with the current module in the program.
    - An **outermost scope** refers to all the available built-in names callable in the program.

***12. What is a dictionary in Python?***
- Python dictionary is one of the supported data types in Python. 
- It is an unordered collection of elements. 
- The elements in dictionaries are stored as key–value pairs. 
- Dictionaries are indexed by keys.

***13. What are functions in Python?***
- A function is a 'block of code' which is executed only when a call is made to the function. 
- Function ensures the 'dry' principle and reusability withing the program
- *def* keyword is used to define a particular function

***14. What is __init__?***
- __init__ is a method or constructor in Python. 
- This method is automatically called to allocate memory when a new object/ instance of a class is created. 
- All classes have the __init__ method.

***15. What are the common built-in data types in Python?***
Python supports the below-mentioned built-in data types:
**Immutable data types:**
-    Number
-    String
-    Tuple

**Mutable data types:**
-    List
-    Dictionary
-    Set

***16. What are local variables and global variables in Python?***
**Local variable:** Any variable declared inside a function is known as Local variable and it’s accessibility remains inside that function only.
**Global Variable:** Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.

***17. What is type conversion in Python?***
Python provides us with a  functionality of converting one form of data type into another and this is known as type conversion.  
Type Conversion is classified into types:  
**1. Implicit Type Conversion:** In this form of Type conversion, python interpreter automatically converts the data type into another one without any user involvement.  
**2. Explicit Type Conversion:** In this Type conversion, the data type in changed into a required type by the user.  

***22. What are Python packages?***
A Python package refers to the collection of different sub-packages and modules based on the similarities of the function.

***23. What are decorators in Python?***
In Python, decorators are necessary functions that help add functionality to an existing function without changing the structure of the function at all. These are represented by @decorator_name in Python and are called in a bottom-up format.

