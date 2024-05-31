import json


def load_operations():
    """Получаем список операций из файла operations"""
    with open("../data/operations.json", "r", encoding="utf-8") as file:
        operations_list = json.load(file)
        return operations_list


def edit_operations():
    """Меняем from на from_ чтобы исключить конфликт"""
    lst = [i for i in load_operations() if i.get("from")]
    for operation in lst:
        operation["from_"] = operation.pop("from")
    return lst


def operations_sort_date():
    """Сортировка от последней даты"""
    lst = [i for i in edit_operations() if i.get("date")]
    return sorted(lst, key=lambda x: x["date"], reverse=True)


def show_last_operation(number=5):
    """Показать последние 5 операций"""
    return [x for x in operations_sort_date()[0: number + 1] if x["state"] == "EXECUTED"]
