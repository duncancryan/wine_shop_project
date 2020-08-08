class Producer:
    def __init__(self, name, country, contact_number, contact_email, active = True, id = None):
        self.name = name
        self.country = country
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.active = active