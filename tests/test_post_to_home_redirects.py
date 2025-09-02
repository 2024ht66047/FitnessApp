def test_post_to_home_redirects(client):
    """Test that a POST request to the home page results in a redirect."""
    response = client.post('/', data={
        'workout': 'Yoga', 
        'duration': '20'
    })
    
    assert response.status_code == 302
    assert response.location == '/'
