
from flask import Flask, request, jsonify
import Hotkeys

app = Flask(__name__)


@app.route('/')
def home():
	return Hotkeys.random_tip()

@app.route('/params/test', methods=['GET'])
def add():
  args = request.args.to_dict()
  return jsonify({"value": float(args["num1"])+float(args["num2"])})

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)