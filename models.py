class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price})>"

    @staticmethod
    def get_all_items():
        return [
            Item("Apple", 1.0),
            Item("Banana", 0.5),
            Item("Orange", 0.75)
        ]
