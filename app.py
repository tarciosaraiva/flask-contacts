from db import Db
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
db = Db()

@app.route('/')
def index():
    contacts = db.data
    return render_template('all_contacts.html', contacts=contacts)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return __save_contact()
    else:
        return render_template('create_contact.html', contact=db.new_contact())

@app.route('/contacts/<uuid:contact_id>', methods=['GET', 'POST', 'DELETE'])
def contact(contact_id):
    if request.method == 'POST':
        hidden_action = request.form.get('action')

        if hidden_action is not None and hidden_action == "delete":
            db.delete_contact(str(contact_id))
            return redirect(url_for('index'))
        else:
            return __save_contact()

    contact = db.load_contact(str(contact_id))

    if contact is None:
        return page_not_found(None)

    return render_template('edit_contact.html', contact=contact)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

def __save_contact():
    db.save_contact(request.form)
    return redirect(url_for('index'))
