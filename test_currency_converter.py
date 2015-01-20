import currency_converter as cc
rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]


def test_one_to_one():
    assert cc.convert(rates, 1, "USD", "USD") == "1 USD"


def test_conversion_simple():
    assert cc.convert(rates, 1, "USD", "EUR") == "0.74 EUR"


def test_conversion():
    assert cc.convert(rates, 0.5, "USD", "EUR") == "0.37 EUR"
    assert cc.convert(rates, 2, "EUR", "JPY") == "291.898 JPY"


def test_conversion_2_dollars():
    assert cc.convert(rates, 2, "USD", "EUR") == "1.48 EUR"


def test_reverse():
    assert cc.convert_reverse(rates, 2, "EUR", "USD") == "2.70 USD"
    assert cc.convert_reverse(rates, 145.949, "JPY", "EUR") == "1.00 EUR"
