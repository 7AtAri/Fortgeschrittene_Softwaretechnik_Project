## Functional Programming Rules applied to the Project:

### 1) Handeling side effects
Since the project relies on user input, 
and the interaction of the bot with the website
it can not be free of side effects.
In fact it relies on side effects, because it 
manipulates the browser object in each of the bots actions.

But the goal is to move the side effects to the edges 
of the project. The user input of necessary information 
is implemented in the beginning. Followed by the business logic
and finally it results in the bots interaction with the website and
some console output. 
Due to the fact, that it is not always possible to book an appointment 
immediately, e.g. if there are no dates available for the chosen 
type of service, the process has to be repeated in some cases.
This is done by a scheduler, that has to be wrapped around the core
project structure.

