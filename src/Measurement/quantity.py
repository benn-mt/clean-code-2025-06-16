class Quantity:
    def __init__(self, amount, unit):
        self._amount = amount
        self._unit = unit

    def __eq__(self, other):
        return False
    
    def __repr__(self):
     return f"Quantity({self._amount} {self._unit}) "