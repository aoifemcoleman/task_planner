# Write your code to expect a terminal of 80 characters wide and 24 rows high

print('Welcome to your daily task planner!')
name = input('What is your name? ')
# https://flexiple.com/python/python-capitalize-first-letter
# https://www.w3schools.com/python/ref_string_format.asp
print('\nHello, {}, what would you like to do today?\n'.format(name.capitalize()))

def show_menu():
    """
    Display menu items and iterate through them to print each on
    new line"
    """
    menu_items = ['1. View task planner', '2. Add task to planner', '3. Mark task as complete', '4. Remove task', '5. Exit task planner']
    for item in menu_items:
        print(item)

def menu_choice():
    """
    Connecting choice made by user with corresponding function
    While loop iterates through choices indefinitely until user 
    selects to leave the planner
    """
    while True:
        choice = input('Please enter a number between 1-5, corresponding to your choice. ')
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            leave_planner()
        else:
            print('You have not entered a valid choice. Please enter a number between 1-5.')
    
def view_tasks(tasks):
    if tasks:
        print('\nYour tasks:')
        """
        Iterating through list of tasks and printing one by one.
        Enumerate method used to count tasks in list, starting from 1
        for better user comprehension in later function.
        Method suggested here: 
        https://stackoverflow.com/questions/73923829/how-to-accept-input-from-an-enumerated-list-in-python
        and learned here: https://realpython.com/python-enumerate/
        """
        for count, task in enumerate(tasks, start=1):
            print(count, task.capitalize())
    else:
        print('You have not yet added any tasks.\n')
        print('Would you like to add a task?\n')
        response = input('Please enter "yes" or "no".  ')
        if response.lower() == "yes":
            add_task(tasks)
        elif response.lower() == "no":
            print('\nWhat would you like to do now?')
            # show_menu()
            # menu_choice()
        else:
            print('You have not entered a valid answer. Please enter "yes" or "no".')

def add_task(tasks):
    new_task = input('\nPlease enter a task: ')
    tasks.append(new_task)
    print('\nYour task has been added')
    print('Would you like to add another task?')
    response = input('Please enter "yes" or "no".  ')
    if response.lower() == "yes":
        add_task(tasks)
    elif response.lower() == "no":
        print('\nWhat would you like to do now?')
    else:
        print('You have not entered a valid answer. Please enter "yes" or "no".')
    # print('\nWhat would you like to do now?')
    show_menu()

def complete_task(tasks):
    print('\nYour tasks:')
    """
    Iterating through tasks to print with corresponding numbers for user
    to make numeric choice from
    """
    # possible separate function can be made for below step, as is repeated
    for count, task in enumerate(tasks, start=1):
            print(count, task.capitalize())
    if tasks:
        completed_task_number = input('Please enter the number corresponding to the task you wish to mark as complete: ')
        if completed_task_number.isnumeric():
            completed_task_number = int(completed_task_number)
            if completed_task_number <= len(tasks):
                completed_task = tasks[completed_task_number]
                tasks[completed_task_number] = f'{completed_task} (Completed)'
                print(f'"{completed_task}" has been marked as complete.')
                updated_tasks = [(count, task.capitalize()) for count, task in enumerate(tasks, start=1)]
                for count, task in updated_tasks:
                    print(count, task)
            else:
                print('Invalid task number. Please enter a valid number.')
        else:
            print('You have not entered a valid answer. Please enter a numeric value.')
    else: 
        print('No tasks to mark as complete')
        # Logic to go back to main menu or leave planner to go here

    

def remove_task():
    print('Select task to remove')
    print('Please enter number corresponding to task number')

def leave_planner():
    print('Would you like to exit the planner?')
    response = input('Please enter "yes" or "no": ')
    if response.lower() == "yes":
        print('Goodbye, best of luck completing your tasks!')
        exit()
    else:
        print('What would you like to do?')
        show_menu()


tasks = []

def main():
    show_menu()
    menu_choice()
    view_tasks(tasks)
    add_task(tasks)
    # complete_task()
    # remove_task()
    # leave_planner()

main()