class Product:
    def __init__(self, name, type, producer, cost, price, case_price, stock, id = None, reduction = 0):
        self.name = name
        self.type = type
        self.producer = producer
        self.cost = cost
        self.price = price
        self.case_price = case_price
        self.stock = stock
        self.id = id
        self.reduction = reduction

    def calculate_markup_individual(self):
        difference = self.price - self.cost
        markup_percentage = (difference/self.cost) * 100
        return round(markup_percentage, 1)

    def calculate_markup_case(self):
        case_cost = self.cost * 6
        difference = self.case_price - case_cost
        case_markup_percentage = difference/case_cost * 100
        return round(case_markup_percentage, 1)

    def enact_reduction(self):
        percentage = self.reduction / 100
        individual_reduction = percentage * self.price
        case_reduction = percentage * self.case_price
        self.price -= individual_reduction
        self.case_price -= case_reduction
    