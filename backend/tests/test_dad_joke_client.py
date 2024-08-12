import pytest
import requests
from unittest.mock import patch, MagicMock
import time

from dad_joke_client import DadJokeClient, DadJokeClientError

def test_initialization():
    client = DadJokeClient(retries=3, delay=1)
    assert client.retries == 3
    assert client.delay == 1
    assert client.base_url == "https://icanhazdadjoke.com/search"
    assert client.headers == {"Accept": "application/json"}

@patch('requests.get')
def test_successful_joke_retrieval(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'results': [{'joke': 'Joke 1'}, {'joke': 'Joke 2'}]}
    mock_get.return_value = mock_response
    
    client = DadJokeClient()
    jokes = client.get_jokes('funny', 2)
    assert len(jokes) == 2
    assert jokes == ['Joke 1', 'Joke 2']

@patch('requests.get')
def test_retry_mechanism(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500  # Simulate server error
    mock_get.return_value = mock_response
    
    client = DadJokeClient(retries=3, delay=0)
    
    with pytest.raises(DadJokeClientError):
        client.get_jokes('funny', 2)
    
    assert mock_get.call_count == 3  # Should retry 3 times

@patch('time.sleep', return_value=None)  # To speed up the test
@patch('requests.get')
def test_rate_limiting(mock_get, mock_sleep):
    mock_response = MagicMock()
    mock_response
