# Write your code to expect a terminal of 80 characters wide and 24 rows high

def show_menu():
    print('Welcome to your daily task planner!')
    name = input('What is your name? ')
    print('\nHello, {}, what would you like to do today?\n'.format(name))
    menu_items = ['1. View task planner', '2. Add task to planner', '3. Mark task as complete', '4. Remove task', '5. Exit task planner']
    for item in menu_items:
        print(item)
    print('\nPlease enter a number between 1-5, corresponding to your choice.')


def view_tasks():
    print('You have not yet added any tasks')

def add_task():
    input('Please enter a task: ')

def complete_task():
    print('Select task to list as complete')
    print('Please enter number corresponding to task number')

def remove_task():
    print('Select task to remove')
    print('Please enter number corresponding to task number')

def leave_planner():
    print('Would you like to exit the planner?')
    input('Please enter y (for yes) or n (for no) ')

def main():
    show_menu()
    # view_tasks()
    # add_task()
    # complete_task()
    # remove_task()
    # leave_planner()

main()