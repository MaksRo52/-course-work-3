from src.operations import Operation
from src import utils


def main():
    lst = utils.show_last_operation()
    operations = Operation.from_dict(lst)
    return [x for x in operations]


if __name__ == '__main__':
    transactions = main()
    for operation in transactions:
        print(f"{operation.edit_date()} {operation.description} \n"
            f"{operation.hide_card_numbers(operation.from_)} -> {operation.hide_account_numbers(operation.to)}\n"
            f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n")
