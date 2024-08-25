"""Module that creates a JSON file from the faker factory."""
import json
import os


def read_json_file(file):
    """Read and return the contents of the JSON file."""
    if os.path.exists(file):
        with open(file, "r") as json_file:
            try:
                data = json.load(json_file)
                if isinstance(data, list):
                    return data
            except Exception as e:
                print(f"Error: JSON file corrupted of empty: {e}.\nReturning empty list.")
    return []


def create_json_file(users, json_file):
    """Writes the JSON file."""
    with open(json_file, "w") as file:
        print(f"writing to a file: {file}")
        json.dump(users, file, indent=4)


def update_user(user_id, updated_data, json_file):
    """Updates an user in the JSON file."""
    users = read_json_file(json_file)
    for user in users:
        if user['id'] == user_id:
            user.update(updated_data)
            create_json_file(users, json_file)
            print(f"User {user_id} updated.")
            return
    print("No users found.")


def delete_user(user_id, json_file):
    """Deletes the user from the JSON file."""
    users = read_json_file(json_file)
    users = [user for user in users if user['id'] != user_id]
    create_json_file(users, json_file)
    print(f"User {user_id} deleted.")


def insert_user(user, json_file):
    """Inserts an user to JSON file."""
    users = read_json_file(json_file)
    if not isinstance(users, list):
        users = []
    users.append(user)
    create_json_file(users, json_file)
    print(f"User {user['id']} inserted.")


def list_users(json_file):
    """Lists the users from the JSON file."""
    users = read_json_file(json_file)
    if users:
        for user in users:
            print(json.dumps(user, indent=4))
    else:
        print("No users found")


def clear_json_file(json_file):
    """Clears the JSON file, leaving it empty."""
    with open(json_file, "w") as json_file:
        json.dump([], json_file, indent=4)
    print("Json file cleared")
