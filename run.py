# Write your code to expect a terminal of 80 characters wide and 24 rows high

print('Welcome to your daily task planner!')
name = input('What is your name? ')
print('\nHello, {}, what would you like to do today?\n'.format(name))

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
        # iterating through list of tasks and printing one by one
        for task in tasks:
            print(task)
    else:
        print('You have not yet added any tasks.\n')
        print('Would you like to add a task?\n')
        response = input('Please enter "yes" or "no".  ')
        if response == "yes":
            add_task(tasks)
        elif response == "no":
            print('\nWhat would you like to do now?')
            # show_menu()
            # menu_choice()
        else:
            print('You have not entered a valid answer. Please enter "yes" or "no".')

def add_task(tasks):
    new_task = input('\nPlease enter a task: ')
    tasks.append(new_task)
    print('\nYour task has been added')
    print('\nWhat would you like to do now?')
    show_menu()

def complete_task():
    print('Select task to list as complete')
    print('Please enter number corresponding to task number')

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