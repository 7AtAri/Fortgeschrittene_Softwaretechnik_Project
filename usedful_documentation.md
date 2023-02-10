
###### SElENIUM DOCUMENTATION: ######

selenium docu:
selenium documentation:
https://selenium-python.readthedocs.io/index.html
https://www.scrapingbee.com/blog/selenium-python/

depending on version of selenium, geckodriver is not necessary to use firefox:
this is the path on my computer where I store the geckodriver for firefox
os.environ['PATH'] += r"/Users/ari/Documents/Data_Science/1_Semester/Fortgeschrittene\ " \
                      r"Softwaretechnik/Fortgeschrittene_Softwaretechnik_Project2 "

css selectors:
https://www.w3schools.com/cssref/css_selectors.php



###### TESTING DOCUMENTATION: ######

# Testing selenium #
https://www.geeksforgeeks.org/writing-tests-using-selenium-python/
https://github.com/MarketingPipeline/Python-Selenium-Action


###### BUIlDING DOCUMENTATION: ######
pybuilder:
https://pybuilder.io/documentation/tutorial


###### SCHEDUlING DOCUMENTATION: ######
used:
https://docs.python.org/3/library/sched.html
not used:
https://schedule.readthedocs.io/en/stable/


###### DECORATORS DOCUMENTATION: ######
general:
https://realpython.com/primer-on-python-decorators/
https://www.freecodecamp.org/news/python-property-decorator/
https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators

# FUNCTOOlS #
https://docs.python.org/3/library/functools.html

helpful if you need the name of the decorated function or 
its docstring:

@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)

## example:
from functools import wraps
>>> def my_decorator(f):
...     @wraps(f)
...     def wrapper(*args, **kwds):
...         print('Calling decorated function')
...         return f(*args, **kwds)
...     return wrapper
...
>>> @my_decorator
... def example():
...     """Docstring"""
...     print('Called example function')
...
>>> example()
Calling decorated function
Called example function
>>> example.__name__
'example'
>>> example.__doc__
'Docstring'