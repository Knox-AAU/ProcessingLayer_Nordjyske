class TokenDict(dict):
    def __init__(self):
        self = dict()

    def add(self, token, amount, rank):
        if token not in self:
            self[token] = {'amount': amount, 'rank': rank}
        else:
            self[token]['amount'] += amount

    def extend(self, dicts):
        for d in dicts:
            self.add(d, dicts[d]['amount'], dicts[d]['rank'])

    def get_total_amount(self):
        amount_sum = 0
        for item in self.items():
            amount_sum += item[1]['amount']
        return amount_sum
            