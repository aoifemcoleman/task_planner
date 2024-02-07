# Write your code to expect a terminal of 80 characters wide and 24 rows high

def show_menu():
    menu_items = ['1. View task planner', '2. Add task to planner', '3. Mark task as complete', '4. Remove task', '5. Exit task planner']
    for item in menu_items:
        print(item)


def main():
    show_menu()

print('Welcome to your daily task planner!')
print('What is your name?')
name = input()
print('Hello,',name, ', what would you like to do today?')
main()