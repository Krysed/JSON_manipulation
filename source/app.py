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
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

    def choose_action(self, action):
        """Execute the selected action based on user input."""
        if action == 1:
            number_of_users = self.read_how_many_users("add")
            self.add_fake_users(number_of_users)
        elif action == 2:
            self.list_users()
        elif action == 3:
            self.delete_or_update_user(1)
        elif action == 4:
            number_of_users = self.read_how_many_users("delete")
            self.delete_or_update_user(2, number_of_users)
        elif action == 5:
            self.exit_action()
        else:
            print("No such option available. Please choose a valid option.")

    def add_fake_users(self, number):
        """Add two fake users using the factories module."""
        for _ in range(number):
            user = factories.create_fake_user()
            json_creator.insert_user(user, self.json_file)
        print("Two fake users have been added.")

    def read_how_many_users(self, operation):
        """Read the value on how many users to add to the JSON."""
        number_of_users = int(input(f"How many users to {operation}?: "))
        return number_of_users

    def list_users(self):
        """List all users from the JSON file."""
        print("Listing all users:")
        json_creator.list_users(self.json_file)

    def delete_or_update_user(self, option, number_of_users=1):
        """Decision function on what manipulation to do next."""
        users = json_creator.read_json_file(self.json_file)
        if not users:
            print("No users available to update or delete.")
            return
        if option == 1:
            self.update_user()
        elif option == 2:
            self.delete_user(number_of_users)


    def delete_user(self, number_of_users):
        """Delete the selected user from the list."""
        self.list_users()
        for _ in range(number_of_users):
            user_id = input("User id for deletion: ")
            json_creator.delete_user(user_id, os.path.join("sample.json"))

    def update_user(self):
        """Delete the selected user from the list."""
        self.list_users()
        user_id = input("Select user id to midify: ")
        name = input("Updated Name: ")
        username = input("Updated username: ")
        email = input("Updated email: ")
        address = input("Updated Address: ")
        phone_number = input("Updated Phone Number: ")
        date_of_birth = input("Updated Date of birth: ")

        updated_data = {
            'id': user_id,
            'name': name,
            'username': username,
            'email': email,
            'address': address,
            'phone_number': phone_number,
            'date_of_birth': date_of_birth
        }
        json_creator.update_user(user_id, updated_data, os.path.join("sample.json"))

    def exit_action(self):
        """Exiting an application"""
        print("Exiting..")
        sys.exit()
