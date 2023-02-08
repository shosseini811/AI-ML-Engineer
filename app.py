from flask import Flask, request # import Flask and request from flask module
import requests # import requests module

app = Flask(__name__) # create an instance of Flask

@app.route('/', methods=['GET'])
def index():
    return     f"""
    <a href="/api/supervisors">GET /api/supervisors</a>
    <br><br>
    <p>Returns a list of supervisors sorted in alphabetical order.</p>
    <h4>Response:</h4>
    <p>A list of supervisor strings formatted as follows:
    "jurisdiction - lastName, firstName"</p>
    <p>Supervisors within the endpoint response payload are sorted in alphabetical order first by jurisdiction, then by lastName and firstName. Numeric jurisdictions are excluded from the response.</p>
    <h4>Example Response:</h4>
    <p>California - Doe, John<br>
    Texas - Smith, Jane<br>
    Washington - Johnson, Bob</p>
    <h4>Status Codes:</h4>
    <p>200 OK: The request was successful and the response contains the sorted list of supervisors.<br>
    404 Not Found: The endpoint was not found.</p>
    <h4>Note:</h4>
    <p>This endpoint calls another API to retrieve the list of managers, which is then formatted and sorted to return the list of supervisors.</p>
    """


@app.route('/api/supervisors', methods=['GET'])
def get_supervisors():
    response = requests.get('https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers') # make a GET request to the specified AWS API
    data = response.json() # convert the response to a JSON object
    supervisors = [f"{item['jurisdiction']} - {item['lastName']}, {item['firstName']}" for item in data if item['jurisdiction'].isalpha()] # create a list of supervisors in the desired format and exclude numeric jurisdictions
    sorted_supervisors = sorted(supervisors, key=lambda x: (x.split(" - ")[0], x.split(" - ")[1].split(", ")[0], x.split(" - ")[1].split(", ")[1])) # sort the supervisors first by jurisdiction, then by lastName and firstName
    return "\n".join(sorted_supervisors) # return the sorted supervisors as a string separated by newline characters

@app.route('/api/submit', methods=['POST'])
def submit_info():
    firstName = request.form.get('firstName') # retrieve the firstName from the form data
    lastName = request.form.get('lastName') # retrieve the lastName from the form data
    email = request.form.get('email') # retrieve the email from the form data
    phoneNumber = request.form.get('phoneNumber') # retrieve the phoneNumber from the form data
    supervisor = request.form.get('supervisor') # retrieve the supervisor from the form data
    if not firstName or not lastName or not supervisor: # check if firstName, lastName, or supervisor is not provided
        return "Error: firstName, lastName, and supervisor are required parameters.", 400 # return an error status code response if any of the required parameters is missing
    print(f"firstName: {firstName}") # print the firstName
    print(f"lastName: {lastName}") # print the lastName
    print(f"email: {email}") # print the email
    print(f"phoneNumber: {phoneNumber}") # print the phoneNumber
    print(f"supervisor: {supervisor}") # print the supervisor
    return "Success", 201 # return success status code



if __name__ == '__main__':
    app.run() # run the Flask application
