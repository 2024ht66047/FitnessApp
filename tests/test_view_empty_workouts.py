from app import workouts

def test_view_empty_workouts(client):
    """Test viewing the page when no workouts are logged."""
    response = client.get('/')
    assert b"No workouts logged yet." in response.data
    assert len(workouts) == 0
