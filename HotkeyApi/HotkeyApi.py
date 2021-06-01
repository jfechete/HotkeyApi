
from flask import Flask, request, jsonify, Response
import Hotkeys

PROGRAM_ARGUMENT = "program"
CATEGORY_ARGUMENT = "category"

app = Flask(__name__)


@app.route("/")
def home():
	return jsonify(Hotkeys.get_random_hotkey())

@app.route("/categories")
def program_categories():
	args = request.args.to_dict()
	if PROGRAM_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(PROGRAM_ARGUMENT),400)
	try:
		return jsonify(Hotkeys.get_categories(args[PROGRAM_ARGUMENT]))
	except ValueError as e:
		return (str(e),400)

@app.route("/programs")
def all_programs():
	return jsonify(Hotkeys.get_all_programs())

@app.route("/hotkeys")
def all_hotkeys():
	args = request.args.to_dict()
	if PROGRAM_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(PROGRAM_ARGUMENT),400)
	if CATEGORY_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(CATEGORY_ARGUMENT),400)
	return jsonify(Hotkeys.get_all_hotkeys_for_category(args[PROGRAM_ARGUMENT],args[CATEGORY_ARGUMENT]))

@app.route("/params/test", methods=["GET"])
def add():
	args = request.args.to_dict()
	return jsonify({"value": float(args["num1"])+float(args["num2"])})

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080)