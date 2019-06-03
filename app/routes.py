from flask import Blueprint, redirect, url_for, render_template, request, g
import pyowm

owm = pyowm.OWM('30f2125f6dc0f2c87bff5355b274ad56')

from app.db import db_singleton

bp = Blueprint('app', __name__, url_prefix='/')

@bp.route('/')
def index():
    contacts = db_singleton.data
    observation = owm.weather_at_place('Melbourne,AU')
    w = observation.get_weather()

    return render_template('all_contacts.html', contacts=contacts, weather=w)

@bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return __delete_or_save_contact()
    else:
        return render_template('create_contact.html', contact=db_singleton.new_contact())

@bp.route('/contacts/<uuid:contact_id>', methods=['GET', 'POST', 'DELETE'])
def contact(contact_id):
    if request.method == 'POST':
        return __delete_or_save_contact()

    contact = db_singleton.load_contact(str(contact_id))

    if contact is None:
        return page_not_found(None)

    return render_template('edit_contact.html', contact=contact)

@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

def __delete_or_save_contact():
    hidden_action = request.form.get('action')

    if hidden_action is not None and hidden_action == "delete":
        db_singleton.delete_contact(str(contact_id))
    else:
        db_singleton.save_contact(request.form)

    return redirect(url_for('app.index'))
