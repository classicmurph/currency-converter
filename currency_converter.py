def convert(rates, value, from_code, to_code):
    """Take a monetary value in one currency and return a value in another
        currency"""
    if from_code == to_code:
        return str(value) + " " + to_code
