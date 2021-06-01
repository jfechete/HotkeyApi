from flask import Flask, request, jsonify, Response
import Hotkeys

#setup
PROGRAM_ARGUMENT = "program"
CATEGORY_ARGUMENT = "category"
KEYS_ARGUMENT = "keys"
LIST_SEPERATOR = ","

app = Flask(__name__)


#connect api to methods
@app.route("/")
def home():
	return jsonify(Hotkeys.get_random_hotkey())

@app.route("/hotkeys")
def all_hotkeys():
	args = request.args.to_dict()
	if PROGRAM_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(PROGRAM_ARGUMENT),400)
	if CATEGORY_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(CATEGORY_ARGUMENT),400)
	return jsonify(Hotkeys.get_all_hotkeys_for_category(args[PROGRAM_ARGUMENT],args[CATEGORY_ARGUMENT]))

@app.route("/categories")
def program_categories():
	args = request.args.to_dict()
	if PROGRAM_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(PROGRAM_ARGUMENT),400)
	try:
		return jsonify(Hotkeys.get_categories(args[PROGRAM_ARGUMENT]))
	except ValueError as e:
		return (str(e),400)

@app.route("/by-keys")
def hotkeys_by_keys():
	args = request.args.to_dict()
	if KEYS_ARGUMENT not in args:
		return Response("Failed to provide a \"{}\" argument".format(KEYS_ARGUMENT),400)

	keys = args[KEYS_ARGUMENT].split(LIST_SEPERATOR)
	try:
		return jsonify(Hotkeys.get_hotkeys_from_keys(keys))
	except ValueError as e:
		return (str(e),400)

@app.route("/programs")
def all_programs():
	return jsonify(Hotkeys.get_all_programs())

@app.route("/params/test", methods=["GET"])
def add():
	args = request.args.to_dict()
	return jsonify({"value": float(args["num1"])+float(args["num2"])})

#run api
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080)