import pytest


from project import get_input
from project import compounding
from project import calculate_monthly_payment


def test_get_input(monkeypatch):
    # monkeypatch from pytest mocks user input
    user_input = iter(["400000", "80000", "5", "30"])

    # mock input function
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    # get the output and assign the output to variables
    loan_amount, annual_interest_rate, loan_period_years = get_input()

    # now assert every output wth expected values
    assert loan_amount == 320000
    assert annual_interest_rate == 0.05
    assert loan_period_years == 30


def test_compounding():
    assert compounding(0.12, 12) == (0.01, 144)


def test_calculate_monthly_payment():
    # result is a float, appx to 2 decimal points
    assert calculate_monthly_payment(
        100000.0, 0.12, 12) == pytest.approx(1313.419141, abs=1e-2)
