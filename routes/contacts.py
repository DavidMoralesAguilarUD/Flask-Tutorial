from flask import Blueprint, render_template, request
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    return render_template('index.html')

@contacts.route('/new', methods=['POST'])
def add():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_Contact = Contact(fullname,email,phone)

    db.session.add(new_Contact)
    db.session.commit()

    return "Saving a contact"

@contacts.route('/update')
def update():
    return "update a contact"

@contacts.route('/delete')
def delete():
    return "delete a contact"


@contacts.route("/about")
def about():
    return render_template('about.html')