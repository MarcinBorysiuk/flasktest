from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
  data = {
    "name": 'Marcin',
    "last_name": 'B',
    "age": 29
  }
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)