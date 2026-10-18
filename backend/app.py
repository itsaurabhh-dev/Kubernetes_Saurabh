from flask import Flask, jsonify 
from flask_cors import CORS 
app = Flask(__name__) 
CORS(app) 
@app.route("/") 
def home(): 
    return jsonify({ 
        "message": "Flask Backend is running successfully!" }) 
@app.route("/api/data") 
def data(): 
    return jsonify({ "message": "Hello from Flask Backend", "status": "success" }) 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)