# Write your code to expect a terminal of 80 characters wide and 24 rows high

def show_menu():
    menu_items = ['1. View task planner', '2. Add task to planner', '3. Mark task as complete', '4. Remove task', '5. Exit task planner']
    for item in menu_items:
        print(item)
    print('\nPlease enter a number between 1-5, corresponding to your choice.')

    

def main():
    show_menu()

print('Welcome to your daily task planner!')
name = input('What is your name? ')
print('\nHello, {}, what would you like to do today?\n'.format(name))
main()