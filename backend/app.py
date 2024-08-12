from flask import Flask, request, jsonify
from dad_joke_client import DadJokeClient, DadJokeClientError
import helper
from flask_cors import CORS
import time
import click

# global config for a running server 
app = Flask(__name__)
cors = CORS(app)
dad_joke_client = DadJokeClient()

# api to get jokes requested by user
# query params: 
# - nums_jokes: int
# - search_term: string
# 
# returns: 
# success: list of jokes
# error: json error, 400 
@app.route('/get_jokes', methods=['GET'])
def get_jokes():
    print("Received request to fetch jokes.")

    # Validate num_jokes
    num_jokes = request.args.get('num_jokes')
    if not helper.is_positive_integer(num_jokes):
        print(f"Invalid num_jokes value: {num_jokes}")
        return jsonify({"error": "num_jokes must be a positive integer"}), 400
    
    num_jokes = int(num_jokes)

    # Validate search_term
    search_term = request.args.get('search_term')
    if not helper.is_alphabetic_string(search_term):
        print(f"Invalid search_term value: {search_term}")
        return jsonify({"error": "search_term must contain only alphabetic characters"}), 400

    # logging
    print(f"num_jokes: {num_jokes}, search_term: {search_term}")

    try:
        jokes = dad_joke_client.get_jokes(search_term=search_term, num_jokes=num_jokes)
        print("Successfully fetched jokes.")
        return jsonify({"jokes": jokes}), 200
    except DadJokeClientError as e:
        print(f"Error fetching jokes: {str(e)}")

        # note: best practice you would not return the error to the client but for ease of use I currently am for frontend clarity
        return jsonify({"error": f"An error occurred while fetching jokes {str(e)}"}), 400


# cli method to get jokes requested by user
# args: 
# - nums_jokes: int
# - search_term: string
#
# i.e. flask get 3 funny 
# 
# returns: 
# success: return and prints jokes with 5 second delay
# error: printed error
@app.cli.command("get")
@click.argument("num_jokes", type=int)
@click.argument("search_term", type=str)
def get_jokes_cli(num_jokes, search_term):
    dad_joke_client = DadJokeClient()

    # Validate num_jokes
    if not helper.is_positive_integer(num_jokes):
        print(f"Invalid num_jokes value: {num_jokes}")
        return
    
    num_jokes = int(num_jokes)

    # Validate search_term
    if not helper.is_alphabetic_string(search_term):
        print(f"Invalid search_term value: {search_term}")
        return

    try:
        jokes = dad_joke_client.get_jokes(search_term=search_term, num_jokes=num_jokes)

        # print jokes with a 5 second delay
        for joke in jokes:
            print(joke)
            time.sleep(5)
        return 
    except DadJokeClientError as e:
        print(f"Error fetching jokes: {str(e)}")

        # note: best practice you would not return the error to the client but for ease of use I currently am for your aid
        print(f"An error occurred while fetching jokes {str(e)}")
        return

if __name__ == '__main__':
    app.run(debug=True)