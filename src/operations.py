from datetime import datetime


class Operation:
    def __init__(self, state, date, operationamount:dict, description, from_, to):
        self.state = state
        self.date = date
        self.operationamount = operationamount
        self.description = description
        self.from_ = from_
        self.to = to


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

