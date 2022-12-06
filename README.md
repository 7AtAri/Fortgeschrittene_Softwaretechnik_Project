# Fortgeschrittene_Softwaretechnik_Project

---------------------------------------------------
## (A) Project: Online Appointment/Reservation Bot

### General:
This project will set up a bot that books (an) appointment(s) for the Berlin Civil Service.
Eventually there will be a time sceduler for the bot, so
it is only active in a configurable repetitve timeframe until the task is done.

e.g. possible use cases: 
- Booking an appointment to register a flat
- Booking an appointment to get a (new) passport
- Booking an appointment to get a (new) ID

### Requirements:
What you will need to install the project:

install the following libraries via pip: 
1) selenium
2) requests
3) beautiful soup 
4) bs4

or use the provided requirements text file:
```diff 
pip install -r requirements.txt
```

please also download and install a selenium webdriver for your specific browser:
https://pypi.org/project/selenium/

Firefox, for example, requires geckodriver, 
which needs to be installed before the code can be run. 
Make sure it’s in your PATH, e. g., 
place it in /usr/bin or /usr/local/bin.

--------------------------------------------------
## (B) Project: Online Appointment/Reservation Bot

### 1 - Git
https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commits/main

### 2 - UML 
```diff 
- at least 3 good different diagrams. 
- "good" means you can pump it up artificially as written in DDD. 
- You have 10 million $ from me! Please export the pics. 
- I can not install all tools to view them!
```

### 3 - DDD 
```diff 
- If your domain is too small, 
- invent other domains around and document these domains 
- (as if you have 100 Mio € from Edlich-Investment!) 
- Develop a clear strategic design with mappings/relationships with >4 Domains 
- coming from an Event Storming. 
- Drop your Domains into a Core Domain Chart 
- and indicate the Relations between the Domains!  
```

### 4 - Metrics
```diff 
- at least two. 
- Sonarcube would be great. 
- Other non-trivial metrics are also fine.
```

### 5 - Clean Code Development: 
```diff 
- A) at least 5 points you can show me with an explanation 
- of why is this is clean code in your code and/or what has improved &  

- B) >>10 points on your personal CCD cheat sheet. E.g. a PDF.
```

### 6 - Build Management
```diff 
- with any Build System as Ant, Maven, Gradle, etc. 
- (only Travis is perhaps not enough) 
- Do e.g. generate Docs, call tests, etc. 
- (it could be also disconnected from the project just to learn a build tool!)
```

### 7 - Unit-Tests
```diff 
- Integrate some nice Unit-Tests in your Code to be integrated into the Build
```

### 8 - Continuous Delivery:
```diff 
- show me your pipeline using 
- e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc.
- E.g. you can also use Jenkins Pipelining or BlueOcean, etc.
- But at least insert more than 2 script calls as done in the lecture! 
- (e.g. also call Ant or Gradle or something else).
```

### 9 - IDE
I use PyCharm as IDE for the project. Since I do the project in Python,
PyCharm is the most obvious choice. Since I have not worked with PyCharm before, I also think this is a good chance to get familiar with it a little.
My favorite Key-Shortcuts are: 
- comment/uncomment 

### 10 - DSL
```diff 
- Create a small DSL Demo example snippet in your code 
- even if it does not contribute to your project
- (hence it can also be in another language).
```

### 11 - Functional Programming:
```diff 
- prove that you have covered all functional aspects in your code as:
- only final data structures
- (mostly) side effect free functions
- the use of higher-order functions
- functions as parameters and return values
- use closures / anonymous functions
- You can also do it outside of your project. 
- Even in another language as F#, Clojure, Julia, etc. 
```







