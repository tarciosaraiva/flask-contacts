import hashlib
import uuid

class Contact:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.date_of_birth = ''
        self.gravatar_hash = ''

    @classmethod
    def from_json(cls, json_entry):
        contact = Contact()
        contact.id = json_entry['id']
        contact.first_name = json_entry['first_name']
        contact.last_name = json_entry['last_name']
        contact.email = json_entry['email']
        contact.date_of_birth = json_entry['date_of_birth']
        contact.gravatar_hash = json_entry['gravatar_hash']
        return contact

    def from_form_request(self, contact_req):
        self.id = contact_req.get('id')
        self.first_name = contact_req.get('first_name')
        self.last_name = contact_req.get('last_name')
        self.email = contact_req.get('email')
        self.date_of_birth = contact_req.get('date_of_birth')
        self.gravatar_hash = hashlib.md5(contact_req.get('email').encode()).hexdigest()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'date_of_birth': self.date_of_birth,
            'gravatar_hash': self.gravatar_hash
        }
