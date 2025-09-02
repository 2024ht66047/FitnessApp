from app import workouts

def test_add_workout_with_invalid_duration(client):
    """Test adding a workout with a non-numeric duration."""
    response = client.post('/', data={
        'workout': 'Cycling', 
        'duration': 'forty'
    }, follow_redirects=True)

    assert b"Duration must be a number." in response.data
    assert len(workouts) == 0
