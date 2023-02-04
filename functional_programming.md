## Useful Functional Programming Rules for Python Projects:
## (with special regards to this project)

### 1) Handeling side effects
Since the project relies on user input, 
and the interaction of the bot with the website
it can not be free of side effects.
In fact it relies on side effects, because it 
manipulates the browser object in each of the bots actions.

But the goal is to move the side effects to the edges 
of the project. The user input of necessary information 
is implemented in the beginning, followed by the business logic
and finally the bots interaction with the website and
some console output. 
Due to the fact, that it is not always possible to book an appointment 
immediately, e.g. if there are no dates available for the chosen 
type of service, the process has to be repeated in some cases.
This is done by a scheduler, that has to be wrapped around the core
project structure.

### 2) try to use recursion / list comprehensions / generators 
###    instead of loops, where it is possible

### 3)a) Only use final data structures
###      Variables are immutable (rather new varibles than modifying old ones)
   -> do not use global variables
   -> from typing import Final
###   b) Use persistent data structures
   -> import pickle
   https://docs.python.org/3/library/pickle.html#comparison-with-marshal

### 4) Passing and returning functions like variables
   https://www.youtube.com/watch?v=n_Y-_7R2KsY

### 5) using the @staticmethod decorator
With the help of static methods we can use a function by calling it through the
class as an API instead of being bound to a specific object.
This way we can have classes, that mix functional and OOP. 
The staticmethod has one single use and can therefor not be overwritten by
a subclass. 

Up until now, the project does not use inheritance or polymorphism.

