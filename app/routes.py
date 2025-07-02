from flask import Flask
from flask import jsonify
from app import create_app

@app.route('api/phone')
def get_phone():
    return 0

@app.route('api/telegram')
def get_telegram():
    return 0;