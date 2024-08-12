import pytest
from app import app
from dad_joke_client import DadJokeClientError
from click.testing import CliRunner
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the Flask routes
def test_get_jokes_success(client, mocker):
    mock_jokes = ["Joke 1", "Joke 2"]
    mock_dad_joke_client = mocker.patch('app.dad_joke_client.get_jokes', return_value=mock_jokes)

    response = client.get('/get_jokes?num_jokes=2&search_term=funny')
    
    assert response.status_code == 200
    assert response.json == {"jokes": mock_jokes}
    mock_dad_joke_client.assert_called_once_with(search_term='funny', num_jokes=2)

def test_get_jokes_invalid_num_jokes(client):
    response = client.get('/get_jokes?num_jokes=abc&search_term=funny')
    
    assert response.status_code == 400
    assert response.json == {"error": "num_jokes must be a positive integer"}

def test_get_jokes_invalid_search_term(client):
    response = client.get('/get_jokes?num_jokes=2&search_term=funny123')
    
    assert response.status_code == 400
    assert response.json == {"error": "search_term must contain only alphabetic characters"}

def test_get_jokes_dad_joke_client_error(client, mocker):
    mock_dad_joke_client = mocker.patch('app.dad_joke_client.get_jokes', side_effect=DadJokeClientError())

    response = client.get('/get_jokes?num_jokes=2&search_term=funny')
    
    assert response.status_code == 400
    assert response.json == {"error": "An error occurred while fetching jokes "}
    mock_dad_joke_client.assert_called_once_with(search_term='funny', num_jokes=2)