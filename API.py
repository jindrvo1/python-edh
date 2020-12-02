from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import json

app = FlaskAPI(__name__)


arr = []

@app.route('/', methods=['GET'])
def hello():
	return json.dumps('hello')

@app.route('/shoppingList', methods=['GET', 'POST', 'PUT', 'DELETE'])
def shoppingList():
	if request.method == 'POST':
		entry = str(request.data.get('entry', ''))
		arr.append(entry)
	if request.method == 'DELETE':
		entry = str(request.data.get('entry', ''))
		if len(entry) < 1:
			arr.clear()
		elif entry in arr:
			arr.remove(entry)
	if request.method == 'PUT':
		entry = request.json
		if 'entry' in entry:
			oldVal = list(entry['entry'].keys())[0]
			newVal = list(entry['entry'].values())[0]

			if oldVal in arr:
				arr.remove(oldVal)
				arr.append(newVal)

	return json.dumps(arr)

if __name__ == "__main__":
    app.run(debug=True)