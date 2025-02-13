from flask import Flask, jsonify, send_from_directory, Response, request, session
from flask_cors import CORS
from pymongo import MongoClient
import os
import boto3
from tempfile import NamedTemporaryFile
from config import DB_URL, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from bson.objectid import ObjectId
from prometheus_client import  generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
app.secret_key = 'your-secret-key'
CORS(app)

# MongoDB connection (use the same DATABASE_URL as in Docker Compose)
client = MongoClient(DB_URL)
db = client['main_db']
users_collection = db['users']
games_collection = db['games']



def add_user_to_db(username, password):
    """Add a new user to the MongoDB database."""
    if users_collection.find_one({"username": username}):
        return False  # User already exists
    users_collection.insert_one({"username": username, "password": password})
    return True

def get_user_by_username(username):
    """Fetch a user by username from MongoDB."""
    user = users_collection.find_one({"username": username})
    if user:
        return {"username": user["username"], "password": user["password"]}
    return None

def get_games():
    """Fetch all available games from MongoDB."""
    games = games_collection.find()
    return [{"id": str(game["_id"]), "name": game["name"], "url": game["url"], "core": game["core"]} for game in games]


def download_from_s3(s3_key):
    """Download a game binary file from S3 to temporary storage."""
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    tmp_file = NamedTemporaryFile(delete=False)  # Do not delete the file after use
    s3_client.download_fileobj(S3_BUCKET_NAME, s3_key, tmp_file)
    tmp_file.close()
    return tmp_file.name  

#simple health check endpoint
@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    """Health check endpoint."""
    return jsonify({"message": "Server is running!"}), 200

#Promethues endpoint
@app.route("/api/metrics", methods=["GET"])
def metrics():
    """Metrics endpoint for Prometheus."""
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}



@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate the user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Fetch the user from MongoDB
    user = get_user_by_username(username)
    if user and user['password'] == password:
        session['username'] = username  # Store username in session
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid username or password"}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    """Logout the user by clearing the session."""
    session.pop('username', None)
    return jsonify({"message": "Logout successful!"}), 200

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    if not add_user_to_db(username, password):
        return jsonify({"message": "Username already taken"}), 400

    return jsonify({"message": "Registration successful!"}), 201

@app.route('/api/games', methods=['GET'])
def get_all_games():
    """API to fetch all games."""
    games = get_games()
    return jsonify(games)

@app.route('/api/games/<game_id>/download', methods=['GET'])
def download_game(game_id):
    """API to download the game binary file from S3 to temporary storage."""
    game = games_collection.find_one({"_id": ObjectId(game_id)})
    if game:
        s3_key = game["s3_url"].split('/', 3)[-1] 
        local_file_path = download_from_s3(s3_key)
        
        return send_from_directory(os.path.dirname(local_file_path), 
                                   os.path.basename(local_file_path), 
                                   as_attachment=True, 
                                   download_name=f"game_{game_id}.bin")
    return Response("Game not found", status=404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
