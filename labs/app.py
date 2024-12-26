from flask import Flask, request, jsonify
import string
import random
import sqlite3
from CRUD import *
from gui_def import PasswordStrengthChecker,Generator

app = Flask(__name__)

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password')
    if not password:
        return jsonify({'error': 'Password is required'}), 400

    strength = PasswordStrengthChecker.check_strength(password)
    strength_text = {0: 'Weak', 1: 'Medium', 2: 'Strong'}
    return jsonify({'password_strength': strength_text[strength]})

@app.route('/generate_password', methods=['GET'])
def generate_password():
    length = request.args.get('length', type=int)
    if not length:
        return jsonify({'error': 'Password length is required'}), 400
    if length < 6 or length > 41:
        return jsonify({'error': 'Password length must be between 6 and 41 characters'}), 400

    password = Generator.generator(length)
    if not password:
        return jsonify({'error': 'Error generating password'}), 500

    return jsonify({'generated_password': password})

app.run(debug=True)
