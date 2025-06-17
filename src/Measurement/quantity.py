class Quantity:
    def __init__(self, amount, unit):
        self._amount = amount
        self._unit = unit

    def __eq__(self, other):
        return self._amount == other._amount and self._unit == other._unit
    
    def __repr__(self):
     return f"Quantity({self._amount} {self._unit}) "