class Contact:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def add_phone_number(self, phone_number):


        self.phone_number = phone_number

if __name__ =='__main__':
    import copy
    paul = Contact('Paul', 'Gries', 'paul@example.com')
    # contact = Contact()
    # paul = Contact(contact, 'Paul', 'Gries', 'paul@example.com')


    # info = ['Paul', 'Gries', 'paul@example.com']
    # paul = Contact(info)


    p = copy.copy(paul)
    paul.add_phone_number('110')
    Contact.add_phone_number(p, '111')

    print(paul.phone_number)
    print(p.phone_number)

    print(str(paul))
