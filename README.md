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

Be aware, that the Bot actually books you an appointment at the Berlin Civil Service.

!!! If you don't want to really book an appointment, please [out-comment this line](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/598a539043de9ffef8297085fe602aaa9dfa07e3/src/main/python/main.py#L81).

### Requirements:
What you will need to install the project:

install the following libraries via pip: 

To simply use the bot:
1) selenium
2) requests
3) beautiful soup 
4) bs4
5) pyrsistent

For the whole CI-Pipeline additionally:

6) pybuilder
7) pyvirtualdisplay
8) geckodriver_autoinstaller

For the DSL-Demo-Example:

9) textX
10) pandas

or use the provided requirements text file:
```diff 
pip install -r requirements.txt
```

Please download and install a selenium webdriver for your specific browser:
[https://www.selenium.dev/selenium/docs/api/py/#drivers](https://www.selenium.dev/selenium/docs/api/py/#drivers)
! Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

--------------------------------------------------
## (B) Project: Online Appointment/Reservation Bot

### 1 - Git
As my git [commit history](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commits) shows,
I frequently added new code over the past months, while working on the project. As you can see, I also added a feature branch for refactoring, 
that was merged back onto the main branch. I also opened a feature branch for a more detailled appointment wish for further development in the future.

### 2 - UML 

In my [UML Diagram folder](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/tree/main/UML_Diagrams) you will find:
- Use Case Diagram
- Activity Diagram
- Class Diagram

### 3 - DDD 

I identified my project's domains with an event storming board and added a mapping with its relations, as well as my Core Domain Chart in the [DDD folder](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/tree/main/event%20storming:DDD).

### 4 - Metrics
I used SonarCloud for metrics and integrated it in my GitHub actions workflow. 
This has the advantage, that the metrics are automatically calculated on every push 
and that the projects metrics are displayed with badges here:

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

A) Clean code examples in my code:
- Replace [Magic Number](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/78fa9ea433ef4b0d0d6018476a5b46a57d7e61fd) by BotSearchInterval class attribute [interval_in_seconds](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/bf32637d7460062c24e1fd9ba7a6a254d175f331/src/main/python/main.py#L74) that is defined by user input.
- Delete [commented out](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/abd6c4d2023cb7f22c0f9ff6980eebc7e4ab1202#diff-d283440e31c4e4b0db72165fa8e9adb638efc0895f3628a8bfd6903f307fd233) feature code and keep it in feature branch only
- [Function refactoring](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/1eca63492484012cd03e442262f2afa28e316180) so that each function only does one thing.
- Followed [naming conventions](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/1eca63492484012cd03e442262f2afa28e316180) in function names for Python code (Pep8)
- Only [one assert per test](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/3194efe07d6b149e74f2e7e78ca3272a78170d68/src/unittest/python/appointmentbot_tests.py#L37) instead of many.

B) My [CCD cheat sheet](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/CCD_cheat_sheet.pdf).


### 6 - Build Management
I chose pybuilder, since pybuilder is a recommended built tool for python
and can also be integrated into the github actions workflow.

My build file can be found [here](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/build.py)
and my [automated builds](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/actions) can be accessed in the github actions
panel by checking the recent build.yml files and following the pybuilder link.


### 7 - Unit-Tests
My project's [unit-tests](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/src/unittest/python/bot_test.py) are integrated in the project's github action workflow. This means that the tests are executed at every push and pull to the repository. This way I can test my own code as well as my code's outside dependencies. If the civil-service website's functionality is changed in a way that effects my project as well, for example, if a button is no longer on the page, the automated tests will let me know.
If you want to run tests locally (with Firefox) use:

python3 -m unittest -v src/unittest/python/bot_test.py

### 8 - Continuous Delivery:

For CD I am using [Github Actions](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/actions). 

I set up sonarcube, pybuilder and unittests to be part of my [Github Actions workflow](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/main/.github/workflows/build.yml).
The workflow is configured to be executed at every push to the repository, so that metrics, tests and a project build are done for every newly uploaded code. 

### 9 - IDE
I use PyCharm as IDE for the project. Since I do the project in Python,
PyCharm is the most obvious choice. I have not worked with PyCharm before, but I think this is a good chance to get familiar with it a little.

I had to personalize some shortcuts.
My favorite Key-Shortcuts are: 

- indent (TAB)/ unindent (SHIFT TAB)
- replace (Command R)
- multiline (out)comment (Command -) 

### 10 - DSL

In my code I used Domain Specific Languages like [Regex](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/b70d9798e5442b6cdc6f25cb50c4bbcd42521b24/src/main/python/user_input.py#L36) and [HTML](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/b70d9798e5442b6cdc6f25cb50c4bbcd42521b24/src/main/python/civilservice_bot.py#L162). 

I also did a [DSL Demo example](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/tree/main/DSL) with
textX, a meta-language for building Domain-Specific Languages (DSLs) in Python. Unfortunately it does not contribute to my project, instead plays with morse code. At the moment it can only be used as a telegraph. Translation of the morse code is still done outside the DSL, but it could maybe be developed to a morse code translater dsl with some more time.


### 11 - Functional Programming:

In my project

- no variables were reassigned. Additionally I used Python's typing package to indicate [Final datastructures](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/7ff084d3a5aa0b905c6f557b05f563dfabd8672b#diff-d283440e31c4e4b0db72165fa8e9adb638efc0895f3628a8bfd6903f307fd233). Type checkers in my IDE check, that my variables are not overwritten or reassigned. For methods and classes in Python a similar effect could be achieved using the @final decorator from the same package.
- I used the [package pyresistent](https://pypi.org/project/pyrsistent/) to convert the list of possible search intervals into a [final datastructure](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/722c25bb40abc4f79f3337deb05c1b847d682611#diff-d283440e31c4e4b0db72165fa8e9adb638efc0895f3628a8bfd6903f307fd233).
- being free of side effects is not possible, since the project relies on user input and the interaction of the bot with the website. In fact it relies on side effects, because it manipulates the browser object in each of the bots actions. Also it all finally had to be wrapped in a Scheduler function, so the bot can try to do its job more than one time, if the appointment booking was not successful in the first place. Still, I tried to keep my functions as side-effect free as possible. 
- when possible I used [list comprehensions instead of loops](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/722c25bb40abc4f79f3337deb05c1b847d682611/src/main/python/user_input.py#L86).
- [Decorators](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/f43e0cda88308f8f093eac985114e60c30875856/src/main/python/civilservice_bot.py#L17) are the main way to use [higher-order functions](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/blob/a84d701302b93d9e41babf7e92d6d559368017b1/src/main/python/decorators.py#L1) in Python. 
- in Python the lambda keyword is used to define an [anonymous function](https://github.com/7AtAri/Fortgeschrittene_Softwaretechnik_Project/commit/471be4a90e4aa09434456fbb1ff51bbbd2ea0d29).








