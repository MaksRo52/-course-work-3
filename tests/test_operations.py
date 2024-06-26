import pytest
from src.operations import Operation

@pytest.fixture
def operation_tst():
    return Operation(
        id=441945886,
        state="EXECUTED",
        date="019-08-26T10:50:58.294041",
        operationAmount={
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        description="Перевод организации",
        from_="Maestro 1596837868705199",
        to="Счет 64686473678894779589",
    )


def coll_operation():
    return [
        Operation(
            id=441945886,
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            operationAmount={
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод организации",
            to="Счет 64686473678894779589",
            from_="Maestro 1596837868705199",
        ),
        Operation(
            id=41428829,
            state="EXECUTED",
            date="2019-07-03T18:35:29.512364",
            operationAmount={
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 35383033474447895560",
            from_="MasterCard 7158300734726758",
        ),
        Operation(
            id=939719570,
            state="EXECUTED",
            date="2018-06-30T02:08:58.425572",
            operationAmount={
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 11776614605963066702",
            from_="Счет 75106830613657916952",
        ),
        Operation(
            id=587085106,
            state="EXECUTED",
            date="2018-03-23T10:45:06.972075",
            operationAmount={
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Открытие вклада",
            to="Счет 41421565395219882431",
            from_=None,
        ),
        Operation(
            id=142264268,
            state="EXECUTED",
            date="2019-04-04T23:20:05.206878",
            operationAmount={
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод со счета на счет",
            to="Счет 75651667383060284188",
            from_="Счет 19708645243227258542",
        ),
        Operation(
            id=873106923,
            state="EXECUTED",
            date="2019-03-23T01:09:46.296404",
            operationAmount={
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод со счета на счет",
            to="Счет 74489636417521191160",
            from_="Счет 44812258784861134719",
        ),
        Operation(
            id=214024827,
            state="EXECUTED",
            date="2018-12-20T16:43:26.929246",
            operationAmount={
                "amount": "70946.18",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 21969751544412966366",
            from_="Счет 10848359769870775355",
        ),
    ]


def test_hide_card_numbers(operation_tst):
    operation = operation_tst
    assert operation.hide_card_numbers(operation.from_) == "Maestro 1596 83** **** 5199"


def test_hide_account_numbers(operation_tst):
    operation = operation_tst
    assert operation.hide_account_numbers(operation.to) == "Счет **9589"