from datetime import datetime


class Operation:
    def __init__(self, id, state, date, operationAmount, description, to, from_):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.from_ = from_
        self.to = to


    @classmethod
    def from_dict(cls, value) -> list:
        """Returns list of class instances"""
        return [Operation(**x) for x in value]


    def edit_date(self):
        """Реформат даты"""
        date = datetime.fromisoformat(self.date)
        format = "%d.%m.%Y"
        return date.strftime(format)


    def hide_card_numbers(self, from_):
        """скрываем номер карты"""
        if from_:
            account_info = "".join(x for x in self.from_ if not x.isnumeric())
            card_numbers = "".join(x for x in self.from_ if x.isnumeric())
            return f"{account_info}{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"


    def hide_account_numbers(self, to: str) -> str:
        """скрываем номер счета"""
        account_info = "".join(x for x in self.to if x.isalpha())
        return f"{account_info} **{self.to[-4:]}"
