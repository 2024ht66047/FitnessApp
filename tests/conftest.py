import pytest
from app import app, workouts

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    # Ensure the workouts list is empty before each test
    workouts.clear()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client