import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(1000, 500, 300)
    assert from_balance == 700
    assert to_balance == 800


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, 0)


def test_transfer_and_interest_workflow():
    from_balance, to_balance = transfer(2000, 1000, 500)
    updated_balance = calculate_interest(to_balance, 10, 1)
    assert round(updated_balance, 2) == 1650.00
