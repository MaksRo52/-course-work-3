from operations import Operation
import json


def load_operations():
    """Получаем список операций из файла operations"""
    with open("../data/operations.json", "r", encoding="utf-8") as file:
        operations_list = json.load(file)
        return operations_list


def operations_lists():
    operation_list = []
    for i in load_operations():
        operation_list.append(Operation(i["state"], i["date"], i["operationAmount"], i["description"], i["from"], i["to"]))
    return operation_list

print(operations_lists())
