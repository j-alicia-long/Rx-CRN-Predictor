from flask import Flask, request, jsonify
from random import randint
app = Flask(__name__)

@app.route('/')
def index():
    return "Aecera API Page"

id = 0
@app.route('/api', methods=['GET'])
def get_score():
    global id
    id += 1
    data = {'id':id, 'score':randint(1,100)}
    return jsonify({'score':data})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')