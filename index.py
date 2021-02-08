import backend
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/Alina", methods=['GET', 'POST'])
@cross_origin()

def output():
	if request.method == 'GET':
		q = str(request.args.get('q'))
		name = str(request.args.get('name'))
		mode = str(request.args.get('mode'))

		setAlina = backend.Alina(q, name, mode)
		alina = setAlina[0]
		mode = setAlina[1]
		long_text = setAlina[2]
		url = setAlina[3]

		return {'alina': alina, 'mode': mode, 'long': long_text, 'url': url}

	# GET request
	else:
		message = {'alina':'Say Hey Alina!'}
		return jsonify(message)  # serialize and use JSON headers

if __name__ == "__main__":
	app.run()