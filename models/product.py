class Product:
    def __init__(self, name, type, producer, cost, price, case_price, stock, id = None):
        self.name = name
        self.type = type
        self.producer = producer
        self.cost = cost
        self.price = price
        self.case_price = case_price
        self.id = id