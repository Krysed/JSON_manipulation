import io
import os
import sys
import json
import pytest

from json_creator import (
    read_json_file,
    create_json_file,
    update_user,
    delete_user,
    insert_user,
    list_users,
    clear_json_file
)


@pytest.fixture
def temp_json_file():
    """Fixture to create and cleanup a temporary JSON file."""
    temp_file = "test_sample.json"
    # Setup: Create an empty file
    with open(temp_file, "w") as file:
        json.dump([], file, indent=4)
    yield temp_file
    # Teardown: Remove the file
    if os.path.exists(temp_file):
        os.remove(temp_file)


def test_read_json_file(temp_json_file):
    """Read the temp json file."""
    assert read_json_file(temp_json_file) == []


def test_create_json_file(temp_json_file):
    """Test if the file was created."""
    users = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'job': 'Tester'}]
    create_json_file(users, temp_json_file)
    with open(temp_json_file, "r") as file:
        data = json.load(file)
    assert data == users


def test_update_user(temp_json_file):
    """Test if the user gets update."""
    users = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'job': 'Tester'}]
    create_json_file(users, temp_json_file)
    update_user(1, {'email': 'updated@example.com'}, temp_json_file)
    updated_users = read_json_file(temp_json_file)
    assert updated_users[0]['email'] == 'updated@example.com'


def test_delete_user(temp_json_file):
    """Test if user gets deleted."""
    users = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'job': 'Tester'},
             {'id': 2, 'name': 'Another User', 'email': 'another@example.com', 'job': 'Tester'}]
    create_json_file(users, temp_json_file)
    delete_user(1, temp_json_file)
    remaining_users = read_json_file(temp_json_file)
    assert len(remaining_users) == 1
    assert remaining_users[0]['id'] == 2


def test_insert_user(temp_json_file):
    """Test if the user gets inserted into json."""
    user = {'id': 1, 'name': 'New User', 'email': 'new@example.com', 'job': 'Developer'}
    insert_user(user, temp_json_file)
    users = read_json_file(temp_json_file)
    assert len(users) == 1
    assert users[0] == user


def test_list_users(temp_json_file):
    """Test if all the users are printed out."""
    users = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'job': 'Tester'},
             {'id': 2, 'name': 'Another User', 'email': 'another@example.com', 'job': 'Tester'}]
    create_json_file(users, temp_json_file)
    # Capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    list_users(temp_json_file)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip()
    expected_output = "\n".join(json.dumps(user, indent=4) for user in users)
    assert output == expected_output


def test_clear_json_file(temp_json_file):
    """Test if the file gets cleaned."""
    users = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'job': 'Tester'}]
    create_json_file(users, temp_json_file)
    clear_json_file(temp_json_file)
    assert read_json_file(temp_json_file) == []
