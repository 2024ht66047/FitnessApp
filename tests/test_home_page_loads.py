def test_home_page_loads(client):
    """Test if the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEestFitness and Gym" in response.data
