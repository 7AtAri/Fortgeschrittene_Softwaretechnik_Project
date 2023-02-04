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
5) pybuilder

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
As my git [commit history](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commits) shows,
I frequently added new code over the past months, while working on the project. As you can see, I also added a feature branch,
that was merged back onto the main branch.

### 2 - UML 

In my [UML Diagram folder](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/tree/main/UML_Diagrams) you will find:
- Use Case Diagram
- Activity Diagram
- Class Diagram

### 3 - DDD 

I identified my project's domains with an event storming board and added a mapping with its relations, as well as my Core Domain Chart in the [DDD folder](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/tree/main/event%20storming:DDD).

### 4 - Metrics
I used Sonarcloud for metrics. This has the advantage, that the projects metrics can be displayed with these batches:
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=7AtAri_Fortgeschrittene_Softwaretechnik_Project&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=7AtAri_Fortgeschrittene_Softwaretechnik_Project)
# 

### 5 - Clean Code Development: 
```diff 
- A) at least 5 points you can show me with an explanation 
- of why is this is clean code in your code and/or what has improved &  

- B) My [CCD cheat sheet](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/CCD_cheat_sheet.pdf).
```

### 6 - Build Management
I chose pybuilder, since pybuilder is a recommended built tool for python
and can also be integrated into the github actions workflow.

My build file can be found [here](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/build.py)
and my [automated builds](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/actions) can be accessed in the github actions
panel by checking the recent build.yml files and following the pybuilder link.


### 7 - Unit-Tests
My [unit-tests](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/src/unittest/python/test_appointmentbot.py) are integrated as an action into the project's github workflow.
This means, that like the build-process and metrics, these are executed at every push to the repository.

### 8 - Continuous Delivery:

For CD I am using Github Actions. 

I already set up sonarcube and pybuilder to be part of my [Github Actions workflow](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/.github/workflows/build.yml).

Next I will add testing to the workflow.
https://docs.github.com/de/actions/automating-builds-and-tests/building-and-testing-python

### 9 - IDE
I use PyCharm as IDE for the project. Since I do the project in Python,
PyCharm is the most obvious choice. I have not worked with PyCharm before, but I think this is a good chance to get familiar with it a little.

I had to personalize some shortcuts.
My favorite Key-Shortcuts are: 

- indent (TAB)/ unindent (SHIFT TAB)
- replace (Command R)
- multiline (out)comment (Command -) 

### 10 - DSL
```diff 
- TODO:
- Create a small DSL Demo example snippet in your code 
- even if it does not contribute to your project
- (hence it can also be in another language).
```

### 11 - Functional Programming:
```diff 
- TODO:
- prove that you have covered all functional aspects in your code as:
- only final data structures
- (mostly) side effect free functions
- the use of higher-order functions
- functions as parameters and return values
- use closures / anonymous functions
- You can also do it outside of your project. 
- Even in another language as F#, Clojure, Julia, etc. 
```







