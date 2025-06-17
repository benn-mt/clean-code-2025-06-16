class Unit:
    def __init__(self, ratioToBaseUnit=1):
        self._ratioToBaseUnit = ratioToBaseUnit

    def amountInBaseUnit(self, amount):
        return amount * self._ratioToBaseUnit