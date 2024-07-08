import pytest

from bank_account import Bank_Acccount


@pytest.fixture
def get_balance():
    balance = 100
    account = Bank_Acccount(balance)
    return account


def test_bank_account(get_balance):

    assert get_balance.balance == 100


def test_deposit_bank_account(get_balance):

    get_balance.deposit(50)
    assert get_balance.balance == 150


def test_withdraw_bank_account(get_balance):

    get_balance.withdraw(30)
    assert get_balance.balance == 70
