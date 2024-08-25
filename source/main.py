"""Main script running the app"""
import os
from factories import create_fake_user
from json_creator import(
    insert_user,
    list_users,
    update_user,
    delete_user,
    read_json_file,
    clear_json_file
    )

json_file = os.path.join("sample.json")

if __name__ == "__main__":
    for _ in range(2):
        insert_user(create_fake_user(), json_file)

    print("Listing all users:")
    list_users(json_file)

    users = read_json_file(json_file)

    print(f"users {users}")
    if users:
        user_id_to_update = users[0]['id']
        updated_info = {'email': 'updated_email@example.com', 'job': 'Updated Job Title'}
        update_user(user_id_to_update, updated_info, json_file)
    print("Listing all users after update:")
    list_users(json_file)

    if users:
        user_id_to_delete = users[0]['id']
        delete_user(user_id_to_delete, json_file)

    print("Listing all users after deletion:")
    list_users(json_file)
    clear_json_file(json_file)
