from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

#Helper function to connect database
def get_db_connection():
    conn = sqlite3.connect('puns.db')
    conn.row_factory = sqlite3.Row #Enables dictionary like access
    return conn

#Route to get all puns
@app.route('/puns', methods=['GET'])
def get_puns():
    conn = get_db_connection()
    puns = conn.execute('SELECT * FROM puns').fetchall()
    conn.close
    return jsonify({'puns': [dict(pun) for pun in puns]})

#Route to get random pun
@app.route('/puns/random', methods=['GET'])
def get_random_pun():
    conn = get_db_connection()
    pun = conn.execute('SELECT * FROM puns ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close
    if pun:
        return jsonify ({'pun' : dict(pun)['pun']})
    return jsonify({'error' : 'No puns found'}), 404

#Serve react static files
@app.route('/')
@app.route('/<path:path>')
def serve_react_app(path=""):
    if path and os.path.exists(f"frontend/build/{path}"):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True);