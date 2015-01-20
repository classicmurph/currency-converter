from decimal import Decimal

rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]
cents = Decimal("0.01")


def convert(rates, value, from_code, to_code):
    """Take a monetary value in one currency and return a value in another
        currency"""
    if from_code == to_code:
        return str(value) + " " + to_code
    else:
        returned_list = [(origin, destination, rate)
                         for (origin, destination, rate)
                         in rates if from_code == origin]
        returned_tuple = returned_list[0]
        returned_rate = returned_tuple[2]
        new_value = returned_rate * value
        return str(new_value) + " " + to_code


def convert_reverse(rates, value, from_code, to_code):
    returned_list = [(destination, origin, rate)
                     for (destination, origin, rate)
                     in rates if to_code == destination]
    returned_tuple = returned_list[0]
    returned_rate = returned_tuple[2]
    new_value = Decimal(value / returned_rate).quantize(cents)
    return str(new_value) + " " + to_code
