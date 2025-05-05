from flask import Blueprint, render_template, request, jsonify
from .ai import AI


main = Blueprint("main", __name__, template_folder="template")
ai = AI()

@main.route("/")
def index():    
    return render_template('index.html')

@main.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()  # Get the JSON data from the request
    user_input = data.get("input")  # Extract the input from the request
    response = ai.callResponse(user_input)

    print(response) # Debugging line to see the response from AI
    
    # Return the response as JSON
    return jsonify(response)
