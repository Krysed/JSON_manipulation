"""Test module for testing factories.py"""
from faker import Faker
from source.factories import create_fake_user


fake = Faker()

def test_create_fake_user():
    """Test if the right fake user gets created."""
    user = create_fake_user()

    assert isinstance(user, dict)
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user
    assert "address" in user
    assert "phone_number" in user
    assert "date_of_birth" in user

    assert isinstance(user["id"], str)
    assert isinstance(user["name"], str)
    assert isinstance(user["username"], str)
    assert isinstance(user["email"], str)
    assert isinstance(user["address"], str)
    assert isinstance(user["phone_number"], str)
    assert isinstance(user["date_of_birth"], str)

    assert len(user["id"]) == 36
    assert fake.email().split('@')[1].split('.')[0] in user["email"]
