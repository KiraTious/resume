from flask import Blueprint, jsonify
from .extensions import db
from .models import Contact

main = Blueprint('main', __name__)


@main.route('/api/phone')
def get_phone():
    contact = Contact.query.get(1)
    return jsonify({'phone' :contact.phone} if contact else 'not found')

@main.route('/api/telegram')
def get_telegram():
    contact = Contact.query.get(1)
    return jsonify({'telegram' : contact.telegram} if contact else 'not found')
