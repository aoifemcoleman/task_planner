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



### Future Features

#### Data storage

In future versions of this application, I would like to offer the user the flexibility of connecting their task planner with either a database, or creating a Google Sheet for efficient storage.

#### Calendar Integration

Another potential feature for future versions would involve enabling users to create to-do lists within the task planner for specific dates. Storing this information in a database or Google Sheet would allow users to conveniently select and act upon lists associated with different dates.

## Data Model

## Testing

### Bugs

#### Solved bugs

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

## Acknowledgements
I would like to once again thank my mentor Ronan McClelland for being so supportive, for his invaluable assistance and inspiration throughout this project.