import app

def test_octocat_gists():
    """Test successful gists fetch for octocat user (main requirement)."""
    client = app.app.test_client()
    response = client.get("/octocat")

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_nonexistent_user():
    """Test API response for non-existent GitHub user."""
    client = app.app.test_client()
    response = client.get("/thisuserdoesnotexist12345")
    
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data

def test_invalid_username():
    """Test API response for username with special characters."""
    client = app.app.test_client()
    response = client.get("/user@invalid")
    
    # Should handle gracefully with error response
    assert response.status_code in [404, 503]
    data = response.get_json()
    assert 'error' in data