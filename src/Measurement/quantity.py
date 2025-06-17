from src.Measurement.unit import Unit

class Quantity:
    def __init__(self, amount: float, unit: Unit):
        self._amount = amount
        self._unit = unit

    def __eq__(self, other):
        return self._amount == other._amount and self._unit == other._unit
    
    def __repr__(self):
     return f"Quantity({self._amount} {self._unit}) "