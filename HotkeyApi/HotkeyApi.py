
from flask import Flask, request, jsonify
import csv
from random import choice

app = Flask(__name__)

tips = []

def get_tips():
  with open("ShortcutData.csv","r",encoding="utf-8") as data_file:
    data_reader = csv.reader(data_file)
    fields = next(data_reader)
    for row in data_reader:
      tip = {}
      for i,value in enumerate(row):
        tip[fields[i]] = value
      tips.append(tip)


@app.route('/')
def home():
	return jsonify(choice(tips))

@app.route('/params/test', methods=['GET'])
def add():
  args = request.args.to_dict()
  return jsonify({"value": float(args["num1"])+float(args["num2"])})

if __name__ == "__main__":
  get_tips()
  app.run(host='0.0.0.0',port=8080)