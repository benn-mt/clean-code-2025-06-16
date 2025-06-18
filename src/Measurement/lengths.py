from src.Measurement.unit import Unit

class Length:
    INCH = Unit()
    FOOT = Unit(12, INCH)
    YARD = Unit(3, FOOT)
    FURLONG = Unit(220, YARD)
    MILE = Unit(8, FURLONG)