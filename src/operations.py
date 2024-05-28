class Operation:
    def __init__(self, state, date, operation_amount:dict, description, from_, to):
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to
