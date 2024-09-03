"""App module"""
import os
import sys
import factories
import json_creator

class App:
    """App class that controls flow of the program."""
    def __init__(self):
        # Initialize the path to the JSON file
        self.json_file = os.path.join("sample.json")

    def start_app(self):
        """Main loop for the program."""
        while True:
            self.show_menu()
            try:
                action = int(input("Choice: "))
                self.choose_action(action)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def show_menu(self):
        """Display the menu options to the user."""
        print("Choose an action to execute:")
        print("1. Add Fake Users")
        print("2. List All Users")
        print("3. Update/Delete User")
        print("4. Exit")

    def choose_action(self, action):
        """Execute the selected action based on user input."""
        if action == 1:
            self.add_fake_users()
        elif action == 2:
            self.list_users()
        elif action == 3:
            self.update_or_delete_user()
        elif action == 4:
            self.exit_action()
        else:
            print("No such option available. Please choose a valid option.")

    def add_fake_users(self):
        """Add two fake users using the factories module."""
        for _ in range(2):
            user = factories.create_fake_user()
            json_creator.insert_user(user, self.json_file)
        print("Two fake users have been added.")

    def list_users(self):
        """List all users from the JSON file."""
        print("Listing all users:")
        json_creator.list_users(self.json_file)

    def update_or_delete_user(self):
        """Update or delete the first user in the list for demonstration purposes."""
        users = json_creator.read_json_file(self.json_file)
        if not users:
            print("No users available to update or delete.")
            return

        print(f"Users: {users}")

        # Update user
        # Delete user

    def exit_action(self):
        """Exiting an application"""
        print("Exiting..")
        sys.exit()
