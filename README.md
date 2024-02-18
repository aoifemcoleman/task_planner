# Task planner

![Screenshot of website responsivity, taken from https://ui.dev/amiresponsive](images/Responsivity.png)

## Purpose
The task planner application is designed to provide users with an easy-to-use, interactive experience within the terminal. Its primary objective is to enable users to effortlessly create a list of tasks, mark them as complete, or remove them as needed.

The application is built using Python. [The live deployed application can be viewed on Heroku here](https://task-planner-116ed91c8a59.herokuapp.com/).

## Features

The functions and features of the application were planned out using a flow-chart before the code was written to implement the desired features:

![Screenshot of website responsivity, taken from https://ui.dev/amiresponsive](images/flowchart.png)

### Existing Features

#### Menu
The app features a main menu that is displayed through the show_menu() function. The main menu contains colour formatting to provide the user with a visually appealing experience, and to indicate when the user has returned to the main menu following interactions with their task planner.

The menu contains five options which facilitate navigation and interaction within the app. It uses user input in the form of integers to seamlessly call the corresponding functions for each menu item, ensuring a user-friendly and intuitive user experience.

![Screenshot of main menu within Heroku terminal](images/menu.png)

#### Task Display

Within the main menu, the first option available to the user is to view the tasks in the task planner, using the integer 1. The function view_tasks(tasks) is subsequently called. 

Upon selecting this option, the user will either be presented with a table of numbered tasks they have added, or, in the absence of any tasks, they will be prompted to add tasks or return to the main menu.

![Screenshot of view tasks selection, when no tasks have been added by the user](images/view-tasks1.png)

![Screenshot of view tasks selection, when tasks have been added by the user](images/view-tasks2.png)

#### Task Addition

The second menu option presented to the user is to add a task to their list, which, using the user input of 2 as an integer, calls the add_tasks(tasks) function. 

If tasks have already been added by the user, a table of these tasks will be created and displayed, before the user is prompted to enter a new task. Once the user has done so, they then have the option of either adding further tasks or to return to the main menu.

![Screenshot of add tasks selection](images/add-tasks.png)

#### Task Completion
The third menu option provided to the user involves marking a task on their list as complete. By inputting the integer 3, the user triggers the complete_tasks(tasks) function.

This function first checks whether all tasks are complete and then whether there have been any tasks added. If there are tasks available which have not yet been marked as complete, the user will be asked to select which task they would like to add the (completed) label to, using corresponding integers.

The user will be able to mark all remaing incomplete tasks, as complete, if they wish to do so. Once they have done so, they will be redirected back to the main menu.

![Screenshot of task being marked as complete](images/complete-tasks1.png)

![Screenshot displaying when all tasks have been marked as complete.](images/complete-tasks2.png)

#### Task Removal

The fourth menu option presented to the user is the ability to remove a task from their list. By entering the integer, the user triggers the calling of the remove_tasks(tasks) function. 

The user is again provided with a table of existing tasks, and can numerically select which task to remove from the list. This can be repeated until the list is empty, and the user will return to the main menu.

![Screenshot of task being removed from list.](images/remove-tasks1.png)

![Screenshot of user returning to main menu when all tasks have been removed](images/remove-tasks2.png)


#### Exiting the application

The fifth and final menu option available to the user is to exit the application, which is triggered by the user input of 5 as an integer. This action calls the leave_planner function.

The user is asked to confirm their choice with "yes" or "no" strings. The former string will present them with a farewell message and discontinue interaction with the app, and the latter will bring them back to the main menu.

![Screenshot of user exiting the app.](images/leave-planner.png)

#### Exception handling
Exception handling exists throughout the various functions and features within the application in order to gracefully handle unexpected errors or input, and provide the user with informative error messages. Some examples of exception handling in this project include:

Invalid Menu Choices:

Within the menu option selection, the user is prompted to input a number within the range of 1-5, corresponding to the menu item of their choice. The code then checks whether a valid integer within this range has been provided. If an invalid response has been received, a ValueError is raised and the user is requested to enter a valid answer.

![Screenshot of exception handling where input of an integer within range of 1-5 is expected and invalid input is received.](images/invalid-menu.png)

- Yes/No Input Validation:

Throughout the application, such as in functions like no_tasks(), add_task(), and leave_or_stay(), the user is asked to confirm specific actions using "yes"/"no" responses. To accommodate variations in capitalization, the user's responses are converted to lowercase. If invalid input is received, a ValueError is raised and the user is prompted to re-enter their response.

![Screenshot of exception handling where yes/no input is expected and invalid input is received.](images/yes-or-no.png)

- Numeric Input Handling:

Where a user is requested to provide a string input but enters an integer, a Value Error is raised with an informative message advising the user the requested input should not include any numeric values.

![Screenshot of exception handling of invalid types.](images/error-numeric.png)

- Task Number Validation:

In the functions complete_tasks(tasks) and remove_tasks(tasks) the user's input is checked to ensure an integer within the range of tasks available has been entered, and if not a Value Error is raised with an informative message.

![Screenshot of exception handling within complete_tasks(tasks) function.](images/error-complete-tasks.png)

### Future Features

#### Data storage

In future versions of this application, I would like to offer the user the flexibility of connecting their task planner with either a database, or creating a Google Sheet for efficient storage.

#### Calendar Integration

Another potential feature for future versions would involve enabling users to create to-do lists within the task planner for specific dates. Storing this information in a database or Google Sheet would allow users to conveniently select and act upon lists associated with different dates.

## Data Model

Fundamental to the task planner is the global `tasks` list, a central data structure that plays a crucial role in the organisation and management of tasks throughout the project. Each main function within the task planner interacts with this list, allowing users to view, add, complete, and remove tasks through its use as a parameter. This data structure is used in the following functions:

- create_table(tasks):

Creates a table using the `tasks` list as a parameter, generating rows corresponding to the length of the tasks list.

- view_tasks(tasks): 

Using the `tasks` list as a parameter, the user can view the tasks that have been added to the tasks list.

- add_task(tasks): 

Enables users to append a task item to the `tasks` list.

- all_tasks_complete(tasks):

The `tasks` list is checked for all tasks which contain (Completed) within their string.

- complete_task(tasks):

A task at a specified index within the `tasks` list is replaced with a string to include (Completed), effectively marking the task in the list as complete.

- remove_task(tasks):

A task at a specified index within the `tasks` list can be removed by the user.

## Testing

I have manually tested the project throughout by doing the following:
- Using a pep8 linter to confirm there are no issues.
- Tested the project throughout it's development in my own terminal, and then in the deployed project terminal on Heroku.

### Menu display

I tested the show_menu() function within the terminal, by entering an integer within the range of 1-5, which correctly triggers the calling of the corresponding function. When an integer outside of this range is entered, or a string value, an error message is displayed to the user:

![Screenshot of error messages for invalid input in main menu.](images/menu-error-message.png)

### Task Display

### Task Addition

### Task Completion

### Task Removal

### Exiting the application

- Providing invalid inputs such as integers where strings are expected and vice versa throughout the application.

### Bugs

#### Solved bugs
- Completed tasks:

Within the complete_tasks(tasks) function, where a user selected to mark a particular task as completed, a user could potentially mark a task as completed multiple times. This was resolved by adding a check for whether the task already contained "(Completed)" before proceeding with the logic.

- Index errors:

Initially when writing my code for the complete_tasks(tasks) function, I was getting errors for example when inputting the integer 1 to select the first task, when there was only item in my list, as the list was displayed starting from 1 rather than 0 as in the list indexing. I solved this by deducting 1 from completed_task_number. I then applied the same resolution to my remove_tasks(tasks) function.

#### Remaining bugs

There are no bugs remaining in the project.

### Validator Testing

The code was run through a [PEP8 linter](https://pep8ci.herokuapp.com/) and initally flagged a number of issues due to the comments surpassing the width of the terminal and some trailing whitespace. The code was updated and subsequently passed with no issues.

## Deployment

This project was deployed using Heroku. The steps taken for deployment are:

- Log in to [Heroku](https://dashboard.heroku.com/apps).
- Select Create new app, provide your app with a unique name and select your region. Then click `Create app`.
- On the next page, navigate to `Settings` in the menu bar, and within `Config Vars` add PORT as the key and 8000 as the value.
- Within `Buildpacks`, add the buildpacks Python and NodeJS, in this order.
- Navigate to `Deploy` in the menu bar.
- Connect Github under `Deployment Method` and provide the link to the repository.
- Within `Manual Deploy` select `Main` and then `Deploy Branch`. Once the branch has been built you can view your deployed project.

## Credits

### Code
- Inspiration for styling using rich library aquired and adopted from [Rich]:(https://rich.readthedocs.io/en/stable/style.html)
- Learned about creating tables and used code snippets from [Rich](https://rich.readthedocs.io/en/stable/tables.html).
- Idea for enumeration found on [Stack Overflow](https://stackoverflow.com/questions/73923829/how-to-accept-input-from-an-enumerated-list-in-python) and method learned and modified from [Real Python]([)](https://realpython.com/python-enumerate/)
- Idea for input validation in menu function taken from here: https://stackoverflow.com/questions/16335771/shorter-way-to-check-if-a-string-is-not-isdigit

## Acknowledgements
I would like to once again thank my mentor Ronan McClelland for being so supportive, for his invaluable assistance and inspiration throughout this project.