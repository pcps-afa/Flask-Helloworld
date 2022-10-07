from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({'msg': 'hello world'}), 200
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')