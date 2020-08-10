class Product:
    def __init__(self, name, type, producer, cost, price, case_price, stock, id = None):
        self.name = name
        self.type = type
        self.producer = producer
        self.cost = cost
        self.price = price
        self.case_price = case_price
        self.stock = stock
        self.id = id

    def calculate_markup_individual(self):
        difference = self.price - self.cost
        markup_percentage = (difference/self.cost) * 100
        return round(markup_percentage, 1)

    def calculate_markup_case(self):
        case_cost = self.cost * 6
        difference = self.case_price - case_cost
        case_markup_percentage = difference/case_cost * 100
        return round(case_markup_percentage, 1)