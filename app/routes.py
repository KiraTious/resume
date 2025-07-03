from flask import Blueprint, jsonify, render_template
from .extensions import db
from .models import Contact

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/phone')
def get_phone():
    contact = Contact.query.get(1)
    return jsonify({'phone' :contact.phone} if contact else 'not found')

@main.route('/api/telegram')
def get_telegram():
    contact = Contact.query.get(1)
    return jsonify({'telegram' : contact.telegram} if contact else 'not found')
