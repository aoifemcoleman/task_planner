# Write your code to expect a terminal of 80 characters wide and 24 rows high

def show_menu():
    menu_items = ['1. View task planner', '2. Add task to planner', '3. Mark task as complete', '4. Remove task', '5. Exit task planner']
    print('What would you like to do today?')
    for item in menu_items:
        print(item)

show_menu()