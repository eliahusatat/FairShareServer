import numpy as np
import sys
from threading import Thread
from _sha256 import sha256

sys.path.append('../')
# from flask import Flask, request, jsonify, send_from_directory
from flask import Flask, redirect, url_for, request , json

# from flask_restful import Resource, Api
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
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

# class Algorithm(Resource):
class Algorithm():

    def get(self):
        return {'algorithm': 'available'}

    def post(self):
        data = request.get_json()
        print(data)
        """
        result = run_algorithm(data)
        url = generate_table(agents=data['agents'], items=data['items'],
                                 data=result, file_name=sha256(str(data['values']).encode('utf-8')).hexdigest(),
                                 data_json=data)

        json_request = {
                'problem': data['problem'],
                'agents': data['agents'],
                'items': data['items'],
                'values': result,
                'RESULT': 0,
                'url': 'http://' + url
            }

        print(json_request)
        req = jsonify(json_request)
        req.status_code = 200
        print("done")
        return req
        """


# api.add_resource(Algorithm, '/calculator')

"""
calculating the algorithm with specific input
:param data represent the JSON that the server receives from the client-side
:return the algorithm result as matrix (numpy.np)
"""





# Used for Debugging only
if __name__ == '__main__':
    app.run(debug=False, port=5000)
