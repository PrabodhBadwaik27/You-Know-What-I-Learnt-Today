# You Know What I Learnt Today
This repository is a pretty-much personal note of what I learnt before starting the backend development with Python for the future reference purpose!

## My Learning Goals
1. [Python Intermediate](https://anandology.com/python-practice-book/index.html)
    - Program Execution
    - Variables
    - Data Structures 
    - Functions
        - Lambda Functions
    - File Handling
    - Object Oriented Programming
    - Exception Handling
    - Iterators
    - Generators
    - Miscellaneous
        - 'in'
        - 'zip'
        - globals() and locals()
    - **Solve Problems on Python, OOP**
    - **Revise Course**
    - *Collections*
    - *RegEx*
2. Review Backend Project/ Other projects (11-09-2021: **Complete Python**, 2 Old projects, 1/2 Backend project recreation)
3. SQL Stored Procedures
    - Syntax
    - **Solve Problems on Stored Procedure**
4. Unstructred Databases
    - Introduction
    - NoSQL/ MongoDb
    - SQL Db. vs NoSQL Db. Differences
    - **Solve Problems on NoSQL**
5. REST
6. Django Theory
7. Migration Project
8. ODBC

# Python Intermediate

## Program Execution

### Compilation and Interpretation
***Python is a Compiled and Interpreted language.***
- The execution process is same as Java.
- Python Code --> Compilation --> Byte Code --> Interpretation --> Execute and generate Result
- Python Execution command: **python file_name.py**

### Different Ways to Run Python Program
1. OS Command Prompt
2. Python cmd Interface
3. Python Shell/ IDLE (Integrated Development and Learning) Platform
4. Anaconda Prompt
5. Jupyter Nb

## Data Structures
1. List []
2. Tuple ()
3. Set {}
4. Dictionary {:}
5. String '', ""

## [Object Oriented Programming](https://pynative.com/python/object-oriented-programming/)
***A PIE : Abstraction, Polymorphism, Inheritance, Encapsulation ***
### Class, Object and Methods
    - isinstance(class, obj)
    - 'del' and desctrutors __del__()
    - [Types of Methods: Class, Instance and Static](https://realpython.com/instance-class-and-static-methods-demystified/)
    - [decorators](https://www.programiz.com/python-programming/decorator)

### [Encapsulation](https://pynative.com/python-encapsulation/)
Access Modifiers
    - public
    - _protected
    - __private
        
***Private***
We can access private members from outside of a class using the following two approaches
    - Create public method to access private members: **Getter and Setter methods**
    - Use name mangling: **obj._class__attribute**

## Miscellaneous

### Lambda Functions
Lambda Functions are the anonymous functions defined without a name to be used for short period of time.

[Refernce](https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8)
[Questions](https://holypython.com/intermediate-python-exercises/exercise-11-python-lambda/)

### [Generators](https://www.programiz.com/python-programming/generator)
Python generators are a simple way of creating iterators. 

Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.  
[Reference](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

#### Iterables, Iterators, Generators and yield keyword
**Iterables:** Any object which can be iterated 
**Iterators:** Iterators are the objects which follows **iterator protocol**
    - **Iterator Protocol:** Iterator Protocol defines implementation of following guidelines for any iterator;
        - An iterator object must implement __iter__() and __next__() methods for data access and traversal
        - **StopIteration** statement/ exception implementation to terminate traversal
**Generators:**
    - Generators provide easy implementation to create **iterator** objects 
    - Generators do not store the complete set of values, but create them on the fly
    - **yield** keyword is used to generate values of the iterator 

### Pickle
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.

# SQL 
## Stored Procedures

## [Cursors](https://www.edureka.co/blog/cursor-in-sql/)


# Unstructured Databases

## MongoDb

### The Document Model
MongoDB stores data in documents (in BSON format files).
BSON (Binary JSON) is a binary representation of JSON (JavaScript Object Notation)

[NoSQL Databases](https://www.mongodb.com/nosql-explained)
[Database and Collections](https://docs.mongodb.com/manual/core/databases-and-collections/)
[CRUD Operations](https://docs.mongodb.com/manual/crud/)
[Bulk Write Operations](https://docs.mongodb.com/manual/core/bulk-write-operations/)
[SQL to NoSQL Queries](https://towardsdatascience.com/8-examples-to-query-a-nosql-database-fc3dd1c9a8c)

# REST 

## REST Architecture
Architecture

## RESTful Web Services
Services that obeys REST constraints
[Reference 1]Wikipedia: REST
[Reference 2](https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)

### Requests Library
[Overview](https://docs.python-requests.org/en/master/user/quickstart/)  
[Implementation Guide](https://www.nylas.com/blog/use-python-requests-module-rest-apis/#how-to-use-python-requests)
[OAuth](https://datatracker.ietf.org/doc/html/rfc6749)
[Different Authorization Methods - e.g. for Spotify](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow)

# Django

### Web Applications
- Dynamic user interaction
- [Web Application v/s Website](https://medium.com/@essentialdesign/website-vs-web-app-whats-the-difference-e499b18b60b4)

### Python Web Frameworks
1. Django (MVC)
2. Flask
3. Django v/s Flask
All references - Edureka

# Database Integration
[ODBC](https://www.magnitude.com/blog/what-is-odbc)  
[ODBC vs. JDBC](https://www.theserverside.com/video/JDBC-vs-ODBC-Whats-the-difference-between-these-APIs)
[Azure vs. SSMS](https://towardsdatascience.com/azure-data-studio-or-ssms-which-should-i-use-1db49824a39)
