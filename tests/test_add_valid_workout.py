from app import workouts

def test_add_valid_workout(client):
    """Test adding a workout with valid data."""
    response = client.post('/', data={
        'workout': 'Running', 
        'duration': '30'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Running" in response.data
    assert b"added successfully" in response.data
    assert len(workouts) == 1
    assert workouts[0]['workout'] == 'Running'
    assert workouts[0]['duration'] == 30