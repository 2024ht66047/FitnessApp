from app import workouts

def test_view_multiple_workouts(client):
    """Test viewing the page with multiple logged workouts."""
    # Add two workouts
    client.post('/', data={'workout': 'Weightlifting', 'duration': '45'})
    client.post('/', data={'workout': 'Swimming', 'duration': '60'})
    
    response = client.get('/')
    
    assert b"Weightlifting" in response.data
    assert b"Swimming" in response.data
    assert len(workouts) == 2