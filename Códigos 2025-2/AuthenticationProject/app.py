from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
Bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = "supersecretkey"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

users = {}

@app.route("/")
def home():
    return "bem vindo a autenticacao API"

@app.route("/register", methods=["POST"])
def register():
    data = request/get_json()
    email = data/get("email")
    password = data.get("password")
    
    if email in users:
        return jsonify({"erro": "usuario ja existe"}), 409
    
    hashed_password = Bcrypt.generate_password_hash(password).decode("utf-8")
    users[email] = {"password": hashed_password}
    
    return jsonify({"mensagem": "usuario registrado com sucesso"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get("password")
    
    user = users.get(email)
    
    if not user or not Bcrypt.check_password_hash(user["password"], password):
        return jsonify ({"erro": "nao autorizado"}), 401
    
    session["user_email"] = email
    return jsonify({"mensagem": "Login com sucesso"}), 200

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user_email", None)
    return jsonify({"mensagem": "Logout com sucesso"}), 200

@app.route("/profile")
def profile():
    if "user_email" not in session:
        return jsonify({"error": "nao autorizado"}), 401
    
    email = session["user_email"]
    return jsonify({
        "message": "Esse é seu perfil!",
        "user":email
    })