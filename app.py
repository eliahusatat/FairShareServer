import numpy as np
import sys
sys.path.append('../')
from flask import Flask, redirect, url_for, request , json

# from flask_restful import Resource, Api
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem


app = Flask(__name__)
# api = Api(app)


"""
This class is a Restful API responsible for the communication with the client.
receive the input from the client(website),
calculating the algorithm, send email in case the algorithm takes more than 5 sec, 
and returns the Algorithm results.
"""

def run_algorithm(data):
    matrix = np.array(data['matrix'])
    if data['type'] == 'envy-free':
        ProblemObject = FairEnvyFreeAllocationProblem(matrix)
        ans = ProblemObject.find_allocation_with_min_shering()
        print('Using EnvyFree Algorithm')
    elif data['problem'] == 'Proportional':
        ProblemObject = FairProportionalAllocationProblem(matrix)
        ans = ProblemObject.find_allocation_with_min_shering()
        print('Using Proportional Algorithm')
    return ans.tolist()

@app.route('/algo',methods = ['POST'])
def algo():
   print('in algo')
   data = request.json
   ans = run_algorithm(data)
   response = app.response_class(
       response=json.dumps(ans),
       status=200,
       mimetype='application/json'
   )
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response


# Used for Debugging only
if __name__ == '__main__':
    app.run(debug=False, port=5000)
