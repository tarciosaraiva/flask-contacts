import json

from app.model.contact import Contact

class Db:

    def setup(self, data_file):
        json_data = json.load(open(data_file, "r"))
        self.data_file = data_file
        self.data = self.__parse(json_data)

    def __parse(self, json_data):
        return list(map(lambda e: Contact.from_json(e), json_data['contacts']))

    def __unparse(self):
        return list(map(lambda c: c.serialize(), self.data))

    def load_contact(self, contact_id):
        return next(filter(lambda contact: contact.id == contact_id, self.data), Contact())

    def delete_contact(self, contact_id):
        contact = self.load_contact(contact_id)
        self.data.remove(contact)
        json.dump({'contacts': self.__unparse()}, open(self.data_file, 'w'))

    def new_contact(self):
        contact = Contact()
        self.data.append(contact)
        return contact

    def save_contact(self, contact_request):
        contact = self.load_contact(contact_request.get('id'))
        contact.from_form_request(contact_request)
        json.dump({'contacts': self.__unparse()}, open(self.data_file, 'w'))

db_singleton = Db()
