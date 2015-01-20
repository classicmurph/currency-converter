import currency_converter as cc
rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]


def test_one_to_one():
    assert cc.convert(rates, 1, "USD", "USD") == "1 USD"
