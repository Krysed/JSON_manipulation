"""App module"""
import os

def define_globals():
    global json_file

class app:    
    def __init__(self):
        self.json_file = os.path.join("sample.json")

    def start_app(self):
        """Main loop for the program."""
        while True:
            self.show_menu()
            action = int(input("Choice: "))
            self.choose_action(action=action)

    def show_menu(self):
        """Display the menu options to the user."""
        print("Choose action to execute:")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. Exit the app.")

    def choose_action(self,action):
        if action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            self.exit_action()
        else:
            print("No such option available.")

    def exit_action(self):
        print("Exiting..")
        exit()
