from flask import Flask, jsonify
from flask_cors import CORS,cross_origin

from Service import ExtractionService

app = Flask(__name__)

@app.route('/extract',methods=['GET'])
@cross_origin()
def extractIneuronData():
    try:
        resultData = ExtractionService.extract_iNeuron_data()
        return jsonify(str(resultData))
    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)
