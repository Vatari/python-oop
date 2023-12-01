class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = Customer.get_next_id()
        Customer.id = 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"
