from rich import print
from rich.console import Console
from rich.table import Table


def show_menu():
    """
    while loop used to repeatedly display menu until
    user enters valid input, ie. integer between 1-5
    """
    while True:
        """
        Creating an instance of Console class from rich library,
        to be used for formatting. Learned about rich here:
        https://rich.readthedocs.io/en/stable/style.html
        """
        console = Console()
        console.print(
            '\nMain Menu:\n', style="bold cyan"
            )
        menu_items = [
            '1. View task planner',
            '2. Add task to planner',
            '3. Mark task as complete',
            '4. Remove task',
            '5. Exit task planner'
            ]
        """
        Display menu items and iterate through them to print
        each on new line, applying style from rich library
        """
        for item in menu_items:
            console.print(
                item, style="magenta"
                )
        """
        Connecting choice made by user with corresponding function
        Exception handling used to populate error message when
        invalid input is entered, ie. string or non-integer
        between 1-5. Method found and modified from here:
        https://stackoverflow.com/questions/16335771/shorter-way-to-check-if-a-string-is-not-isdigit
        """
        try:
            user_input = input(
                '\nPlease enter a number between 1-5,corresponding'
                ' to your choice.\n'
                )
            if not user_input.isdigit():
                raise ValueError(
                    'You have not entered a valid choice.'
                    'Input must be a whole number between 1-5.'
                    )
            choice = int(user_input)
            if 1 <= choice <= 5:
                if choice == 1:
                    view_tasks(tasks)
                elif choice == 2:
                    add_task(tasks)
                elif choice == 3:
                    complete_task(tasks)
                elif choice == 4:
                    remove_task(tasks)
                elif choice == 5:
                    leave_planner()
            else:
                raise ValueError(
                    'You have not entered a valid choice.'
                    ' Input value must be a whole number between 1-5.'
                    )
        except ValueError as e:
            print(f"Error: {e}")


"""
Global task list used as parameter in several functions
to store and manage user input - for viewing, adding,
completing and removing tasks.
"""


def create_table(tasks):
    if tasks:
        """
        Creating table object from rich library
        Method learned and adapted from here:
        https://rich.readthedocs.io/en/stable/tables.html
        """
        table = Table(title="Your tasks")
        table.add_column("Task Number", justify="center", style="cyan")
        table.add_column("Task Name", justify="center", style="magenta")
        """
        Iterating through list of tasks and printing one by one.
        Enumerate method used to count tasks in list, starting from 1
        for better user comprehension in later function.
        Method suggested here:
        https://stackoverflow.com/questions/73923829/how-to-accept-input-from-an-enumerated-list-in-python
        and learned here: https://realpython.com/python-enumerate/
        """
        for count, task in enumerate(tasks, start=1):
            table.add_row(str(count), task.capitalize())

        console = Console()
        console.print(table)


def view_tasks(tasks):
    if tasks:
        create_table(tasks)
        leave_or_stay()
    else:
        no_tasks()
        leave_or_stay()


def no_tasks():
    print(
        '\nYou have not yet added any tasks.'
        )
    print(
        '\nWould you like to add a task?'
        )
    while True:
        response = input(
            '\nPlease enter "yes" or "no".\n'
            )
        try:
            """
            lower method used to accommodate various
            use of capitilisation
            """
            if response.lower() == "yes":
                add_task(tasks)
            elif response.lower() == "no":
                leave_or_stay()
                """
                checking if any character in response
                is a digit, and if so raising value error
                """
            elif any(char.isdigit() for char in response):
                raise ValueError(
                    'Invalid input. Input cannot contain'
                    ' numeric values.'
                    )
            else:
                raise ValueError(
                    'Invalid input. Input must be "yes" or "no",'
                    ' without any special characters, spaces or'
                    ' numeric values.'
                    )
        except ValueError as e:
            print(f"Error: {e}")


def add_task(tasks):
    """
    check if tasks list contains list items,
    and if true, displaying these items to user in a
    table
    """
    if tasks:
        create_table(tasks)
    """
    adding new task to tasks list using user input
    """
    new_task = input('\nPlease enter a task:\n')
    tasks.append(new_task)
    print(
        '\nYour task has been added.'
        )
    print(
        '\nWould you like to add another task?'
        )
    """
    While loop repeats until user has entered valid response.
    Exception handling used to raise error if invalid input from
    user received"
    """
    while True:
        response = input(
            '\nPlease enter "yes" to continue or "no",'
            ' to return to main menu.\n'
            )
        try:
            if response.lower() == "yes":
                add_task(tasks)
            elif response.lower() == "no":
                show_menu()
            elif any(char.isdigit() for char in response):
                raise ValueError(
                    'Invalid input. Please enter "yes" or "no",'
                    ' without any numeric values.'
                    )
            else:
                raise ValueError(
                    '\nYou have not entered a valid answer.'
                    ' Please enter "yes" or "no".'
                    )
        except ValueError as e:
            print(f"Error: {e}")


def all_tasks_complete(tasks):
    """
    Function checks whether all tasks already contain the string (Completed)
    which when called in separate functions will redirect user to main menu,
    as no further can be taken.
    """
    return all("(Completed)" in task for task in tasks)


def complete_task(tasks):

    if all_tasks_complete(tasks):
        print(
            '\nAll tasks have already been marked as complete.'
            ' Returning to main menu.'
            )
        show_menu()

    if tasks:
        create_table(tasks)
        while True:
            completed_task_number = input(
                '\nPlease enter the number corresponding to the task'
                ' you wish to mark as complete:\n'
                )
            try:
                if completed_task_number.isnumeric():
                    completed_task_number = int(completed_task_number)
                    """
                    checking if user input is numeric and then
                    whether it is in within valid range of amount of task
                    items in task list
                    """
                    if completed_task_number <= len(tasks):
                        """
                        Deducting 1 from completed_task_number as list is
                        displayed to user starting from 1 rather than 0 as
                        per list ordering
                        """
                        completed_task = tasks[completed_task_number - 1]
                        """
                        Check to prevent user marking task as complete
                        multiple times
                        """
                        if "(Completed)" not in completed_task:
                            """
                            Creating new string for task to include
                            (Completed).
                            Updating task at specified index in task list
                            to include new string.
                            Backslash used to continue code on new line
                            due to limited terminal width.
                            """
                            tasks[completed_task_number - 1] = \
                                f'{completed_task} (Completed)'
                            print(
                                f'\n"{completed_task.capitalize()}" has been'
                                ' marked as complete.'
                                )
                            updated_tasks = [
                                (count, task.capitalize())
                                for count, task in enumerate(tasks, start=1)
                                ]
                            break
                        else:
                            print(
                                f'"{completed_task.capitalize()}" has already'
                                ' been marked as complete.'
                                )
                            complete_another_task()
                    else:
                        raise ValueError(
                            'Invalid task number. Please enter a'
                            ' valid number.'
                            )
                else:
                    raise ValueError(
                        'You have not entered a valid answer.'
                        ' Please enter a numeric value.'
                        )
            except ValueError as e:
                print(f"Error: {e}")
    else:
        print('\nYou have not added any tasks to mark as complete.')
        show_menu()
    complete_another_task()


def complete_another_task():
    if all_tasks_complete(tasks):
        print(
            '\nAll tasks have been marked as complete.'
            ' Returning to main menu.'
            )
        show_menu()
    else:
        print(
            '\nWould you like to mark another task as complete?'
            )
        while True:
            response = input(
                '\nPlease enter "yes" to continue or "no",'
                ' to return to main menu.\n'
                )
            try:
                if response.lower() == "yes":
                    complete_task(tasks)
                elif response.lower() == "no":
                    show_menu()
                elif any(char.isdigit() for char in response):
                    raise ValueError(
                        'Invalid input. Input cannot contain'
                        ' numeric values.'
                        )
                else:
                    raise ValueError(
                        'Invalid input. Input must be "yes" or "no",'
                        ' without any special characters, spaces or'
                        ' numeric values.'
                        )
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print('\nNo tasks to mark as complete.')
            leave_or_stay()


def remove_task(tasks):
    print(
        '\nYou have selected to remove a task from your list.'
        )
    create_table(tasks)
    if tasks:
        while True:
            remove_task_number = input(
                '\nPlease enter the number corresponding to the'
                ' task you wish to remove:\n'
                )
            """
            checking if user input is numeric and then whether
            it is in within valid range of amount of task
            items in task list
            """
            try:
                if remove_task_number.isnumeric():
                    remove_task_number = int(remove_task_number)
                    if remove_task_number <= len(tasks):
                        """
                        Deducting 1 from remove_task_number as the list is
                        displayed starting from 1 rather than 0 as per list
                        indexing.
                        Removing task at specified index in task list.
                        """
                        removed_task = tasks.pop(remove_task_number - 1)
                        print(
                            f'\n"{removed_task.capitalize()}"'
                            ' has been removed.'
                            )
                        updated_tasks = [
                            (count, task.capitalize())
                            for count, task in enumerate(tasks, start=1)
                            ]
                        break
                        if tasks:
                            remove_another_task()
                    else:
                        raise ValueError(
                            '\nInvalid task number.'
                            )
                else:
                    raise ValueError(
                        '\nYou have not entered a valid answer.'
                        ' Please enter a numeric value.'
                        )
            except ValueError as e:
                print(f"Error: {e}")
    else:
        print(
            '\nNo tasks have been added.'
            )
        leave_or_stay()


def remove_another_task():
    """
    Function handles removing further tasks from
    the task list, validating user input and using
    exception handling with value errors to inform
    users of invalid input
    """
    if tasks:
        print(
            '\nWould you like to remove another task?'
            )
        while True:
            response = input(
                '\nPlease enter "yes" to continue or "no",'
                ' to return to main menu.\n'
                )
            try:
                if response.lower() == "yes":
                    remove_task(tasks)
                    """
                    breaking while loop once user has entered valid
                    input
                    """
                    break
                elif response.lower() == "no":
                    leave_or_stay()
                elif any(char.isdigit() for char in response):
                    raise ValueError(
                        'Invalid input. Input cannot contain'
                        ' numeric values.'
                        )
                else:
                    raise ValueError(
                        'Invalid input. Input must be "yes" or "no",'
                        ' without any special characters, spaces or'
                        ' numeric values.'
                        )
            except ValueError as e:
                print(f"Error: {e}")


def leave_planner():
    """
    Function confirms with user whether they would like
    to leave the task planner, using yes/no input, which
    is validated. A while loop is used to continue prompting
    the user to enter a valid answer
    """
    print(
        '\nWould you like to exit the planner?'
        )
    while True:
        response = input(
            '\nPlease enter "yes" or "no":\n'
            )
        try:
            if response.lower() == "yes":
                print(
                    '\nClosing the task planner...\n'
                    '\nGoodbye, best of luck completing your tasks!'
                    )
                exit()
            elif response.lower() == "no":
                print(
                    '\nReturning to main menu...'
                    )
                show_menu()
            elif any(char.isdigit() for char in response):
                raise ValueError(
                    'Invalid input. Please enter "yes" or "no",'
                    ' without any numeric values.'
                    )
            else:
                if any(char.isdigit() for char in response):
                    raise ValueError(
                        'Invalid input. Please enter "yes" or "no",'
                        ' without any numeric values.'
                        )
                else:
                    raise ValueError(
                        'Invalid input. Input must only contain "yes" or "no".'
                        )
        except ValueError as e:
            print(f"Error: {e}")


def leave_or_stay():
    """
    Function confirms with user whether they would like to
    return to the main menu or leave the planner.
    """
    print(
        '\nWould you like to return to the main menu or leave the planner?'
        )
    while True:
        answer = input(
            '\nPlease enter "return" for the main menu, or "leave" to exit.\n'
            )
        try:
            if answer.lower() == "return":
                print(
                    '\nReturning to main menu...'
                    )
                show_menu()
            elif answer.lower() == "leave":
                print(
                    '\nGoodbye, best of luck completing your tasks!'
                    )
                exit()
            else:
                raise ValueError(
                    'Invalid input. Please enter "return" for the main menu,'
                    ' or "leave" to exit planner.'
                    )
        except ValueError as e:
            print(f"Error: {e}")


# global tasks list
tasks = []


def main():
    print(
        'Welcome to your daily task planner!'
        )
    """
    While loop iterates until user provides valid input.
    Error message printed if any character in the name
    contains a number.
    """
    while True:
        name = input(
            '\nWhat is your name?\n'
            )
        if any(char.isdigit() for char in name):
            print(
                '\nUh oh, your name cannot contain any numbers.'
                ' Please try again using letters only.'
                )
        else:
            break
    """
    Method for string formatting learned and modified from here:
    https://www.w3schools.com/python/ref_string_format.asp
    """
    print(
        '\nHello, {}, what would you like'
        ' to do today?'.format(name.capitalize())
        )
    show_menu()


main()
