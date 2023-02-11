###### DSl - textx ######

http://textx.github.io/textX/3.1/grammar/
https://tomassetti.me/domain-specific-languages-in-python-with-textx/

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

calender dates picking:
https://www.youtube.com/watch?v=0b2No_0cVcc  (Python)
https://www.youtube.com/watch?v=yW1-IbI_soc
https://www.youtube.com/watch?v=HqzlDEPdJ3w
https://www.youtube.com/watch?v=P4hQI-0X3w0

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
chaining decorators:
https://www.programiz.com/python-programming/decorator

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