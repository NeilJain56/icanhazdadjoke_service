# Icanhazdadjoke_service

Author: Neil Jain

## Summary
The Icanhazdadjoke_service is a React.js and Flask app that allows users to get a specific number of dad jokes based on a search term they provide given 5 seconds apart. 

## Features
- Complete frontend/backend app
- CLI support

## Usage
### Web Application: 
After following the running locally steps below for Complete End To End Application:
Enter a number of jokes you would like and a search term and click submit to get your jokes spaced out 5 seconds at a time.

### CLI
After following the running locally steps below for CLI:
In your terminal in the virtual environment use the command:
`flask get [number of jokes] "[search term]"`
Where number of jokes is the number of jokes you want and *search term is surrounded by quotes* and is the term you want to search for.

## Running Locally 

### Complete End To End Application
#### Requirements:
- Python
- Npm


##### Step 1
*Clone the git repository*
```bash
git clone https://github.com/NeilJain56/icanhazdadjoke_service.git
```


##### Step 2 
*Navigate to icanhazdadjoke_service*
```bash
cd icanhazdadjoke_service
```

##### Step 3
*Run setup.py*
```bash
python setup.py
```

##### Step 4 
*Enter backend folder*
```bash
cd backend
```

##### Step 5
*Activate virtual environment*
```bash
source venv/bin/activate
```

##### Step 6
*Run backend server*
```bash
python app.py
```

##### Step 7
*Open new terminal and run the frontend*
```bash
cd ..
cd frontend
npm start
```


### CLI
#### Requirements:
- Python
- NPM

##### Step 1
Clone the git repository
```bash
git clone https://github.com/NeilJain56/icanhazdadjoke_service.git
```

##### Step 2 
*Navigate to icanhazdadjoke_service*
```bash
cd icanhazdadjoke_service
```

##### Step 3
*Run setup.py*
```bash
python setup.py
```

##### Step 4 
*Enter backend folder*
```bash
cd backend
```

##### Step 5
*Activate virtual environment*
```bash
source venv/bin/activate
```

##### Step 6
*Run CLI Command*
```bash
flask get [num_jokes] [search_term]
```

## Design
This service features both a frontend and backend component. The frontend is built using React.js/Tailwindcss/DaisyUI to provide responsive UI/UX. The backend is built entirely with Python/Flask. The backend supports both an API which the frontend consumes as well as 

### Frontend
The frontend is built using React.js/Tailwindcss/DaisyUI to provide responsive UI/UX. The core of this code lies in frontend/src/pages/FormPage.js. There are several other folders that I have added that are empty but in the future if we were to build on this service would prove to be very useful. FormPage renders a simple frontend with a form that takes that input and queries our backend Flask server sending relevant information as query parameters. For input validation the frontend makes sure that only the characters valid can be entered. Once a response is given back from our backend the frontend either shows an error or gets a list of jokes that it displays 5 seconds at a time.

### Backend
The backend is built with Python/Flask and provides both frontend and CLI support. For both the CLI and API the backend throws an error for any erroneous input therefore not trusting the user or frontend for clean input. 

#### API
The API has 1 current route
`/get_jokes?num_jokes=[int]&search_term=[string]`
Which takes in num_jokes and search_term as query parameters. The API validates input, logs relevant information for robust error checking (currently using print statements), and uses the dad_joke_client to make calls. The API also handles all exceptions seemlessly and by choice exposes exceptions to the frontend.

#### CLI
The CLI works very similar to the API except all exceptions are given as print statements instead of json return values. The CLI also does not need to have a running server.

#### dad_joke_client
This client is the core of us getting dad jokes from the https://icanhazdadjoke.com/search API. This client features retry methods as well as robust error handling utilizing its own error class (DadJokeClientError) and pagination handling. The client is also configurable for the delay in retries as well as the amount of retires to allow scalability and avoid rate limits.

#### Testing
Using pytest the backend also has written unit tests that test the helper, app and client. You can run unit tests by typing:
`pytest`


## Next Steps
In the future adding more robust logging and focusing on deployment are top priorities. 
