class Producer:
    def __init__(self, name, country, contact_number, contact_email, id = None, active = True):
        self.name = name
        self.country = country
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.id = id
        self.active = active

    def mark_inactive(self):
        self.active = False

    def mark_active(self):
        self.active = True