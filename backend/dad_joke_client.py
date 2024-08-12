import requests
import time

# Custom exception for DadJokeClient errors
class DadJokeClientError(Exception):
    pass

# Client class for dad joke API 
class DadJokeClient:

    # global client config 
    # retires default 5 with time delay of 2 seconds for rate limiting
    def __init__(self, retries=5, delay=2):
        self.base_url = "https://icanhazdadjoke.com/search"
        self.headers = {
            "Accept": "application/json"
        }
        self.per_page = 10  # Fixed limit for each request
        self.retries = retries  # Number of retries for failed requests
        self.delay = delay  # Delay in seconds between retries

    # gets a list of jokes and raises a DadJokeClientError if any exception or error occurs
    def get_jokes(self, search_term, num_jokes):
        jokes = []
        page = 1

        # account for pagination
        while len(jokes) < num_jokes:
            results = self._fetch_jokes(search_term=search_term, page=page)
            if results is None:
                raise DadJokeClientError("Failed to retrieve jokes after multiple attempts.")
            if not results:
                break  # Stop if no more jokes are found

            jokes.extend(results)
            page += 1

        # if there arent enough jokes return an error
        if len(jokes) < num_jokes:
            raise DadJokeClientError(f"Only {len(jokes)} jokes found, but {num_jokes} were requested.")

        # return jokes by stripping any extra jokes from the list out
        return jokes[:num_jokes]

    # function to handle retry logic for requests as well as exceptions from calls
    def _fetch_jokes(self, search_term, page):
        for attempt in range(self.retries):
            try:
                response = self._make_request(search_term=search_term, page=page)
                if response.status_code == 200:
                    results = response.json().get('results', [])
                    return [joke['joke'] for joke in results]
                else:
                    print(f"Error: Received status code {response.status_code} (Attempt {attempt + 1})")
            except requests.RequestException as e:
                print(f"Request failed: {e} (Attempt {attempt + 1})")
            
            # time delay to avoid rate limits
            time.sleep(self.delay)
        
        return None

    # simple request function
    def _make_request(self, search_term, page):
        params = {
            "term": search_term,
            "limit": self.per_page,
            "page": page
        }
        return requests.get(self.base_url, headers=self.headers, params=params)