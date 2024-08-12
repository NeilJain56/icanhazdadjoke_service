# Icanhazdadjoke_service

## Summary
The Icanhazdadjoke_service is a React.js and Flask app that allows users to get a specific number of dad jokes based on a search term they provide. 

## Features
- Complete frontend/backend app
- CLI support

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


