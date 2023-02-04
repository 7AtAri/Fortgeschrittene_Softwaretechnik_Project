## Clean Code Cheat Sheet

### 1) Boy Scout rule
leave the code cleaner as you found it!

### 2) Follow conventions
follow existing coding conventions
to help others read and understand the code faster!

### 3) DRY
Don't Repeat Yourself! 
Rather use functions and call them various times.

### 4) Tell, don't ask
Tell an object what to do, 
instead of asking for its inner state and then act on it.

### 5) YAGNI
Only implement what is really necessary. 
Develop code step by step instead of implementing 
lots of features from the beginning.

### 6) No Magic Numbers!
Do not put numbers in code. 
A number's meaning should not be a guessing game.
Use variables or even a function instead!

(example changed in the project code: scheduler time interval)

### 7) The code is the best comment!
The code should be readable in a way, that there are (almost) no comments needed.
Use self-explanatory variable, function and class names to achieve that.

### 8) Do one thing and do it well!
Functions should either answer something or do something, but not both.
They should in general only do one thing and they should be well implemented.

### 9) Don’t comment out dead code, delete it!
If the code is maybe needed in the future, 
that’s what version control is for.

### 10) Declare Variables close to where they’re used! 
For small functions, this is usually at the top of the function.

### 11) Use Pep8 style guide for Python
-> class names: CamelCase
-> variable names: snake_case
-> function names: snake_case
-> module names: snake_case
-> constant names: snake_case and all uppercase
https://peps.python.org/pep-0008/

### 12) POLA - Principle of least astonishment
Any component of the system should behave in a way 
that (most) users will expect it to behave.