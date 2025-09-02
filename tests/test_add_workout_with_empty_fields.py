from app import workouts

def test_add_workout_with_empty_fields(client):
    """Test adding a workout with missing fields."""
    response = client.post('/', data={
        'workout': '', 
        'duration': '30'
    }, follow_redirects=True)

    assert b"Please enter both workout and duration." in response.data
    assert len(workouts) == 0