"""Main script running the app"""
import os
import factories
import json_creator


json_file = os.path.join("sample.json")

if __name__ == "__main__":
    for _ in range(2):
        json_creator.insert_user(factories.create_fake_user(), json_file)

    print("Listing all users:")
    json_creator.list_users(json_file)

    users = json_creator.read_json_file(json_file)

    print(f"users {users}")
    if users:
        user_id_to_update = users[0]['id']
        updated_info = {'email': 'updated_email@example.com', 'job': 'Updated Job Title'}
        json_creator.update_user(user_id_to_update, updated_info, json_file)
    print("Listing all users after update:")
    json_creator.list_users(json_file)

    if users:
        user_id_to_delete = users[0]['id']
        json_creator.delete_user(user_id_to_delete, json_file)

    print("Listing all users after deletion:")
    json_creator.list_users(json_file)
    json_creator.clear_json_file(json_file)
