"""Factory that creates fake user objects."""
from faker import Faker

fake = Faker()

def create_fake_user():
    """Creates a fake user with a set of properties for JSON file."""
    user = {
        'id': fake.uuid4(),
        'name': fake.name(),
        'username': fake.user_name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone_number': fake.phone_number(),
        'date_of_birth': str(fake.date_of_birth(
            minimum_age=18, maximum_age=100))
    }
    return user
