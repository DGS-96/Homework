from functools import total_ordering

@total_ordering
class Money:
    exchange_rate = {
        "USD": 1,
        "EUR": 0.8642,
        "BYN": 2.4699,
        "RUB": 71.9039,
        "CNY": 6.5639
    }

    def __init__(self, money_account, currency="USD"):
        """Init Money class"""
        self.money_account = money_account
        self.currency = currency

    def __str__(self):
        return f"{self.money_account} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.money_account + other.money_account *
            	Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency],
            	self.currency)
        if isinstance(other, (int, float)):
            return Money(self.money_account + other, self.currency)
        raise AttributeError

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.money_account * (other.money_account *
            	Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]),
            	self.currency)
        if isinstance(other, (int, float)):
            return Money(self.money_account * other, self.currency)
        raise AttributeError

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.money_account < other.money_account * Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        elif isinstance(other, (int, float)):
            return self.money_account < other
        raise AttributeError


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11) # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8) # result 0.8642
    #>>> 543.21 EUR
    # Exchange rate does not match

    lst = [Money(10,"BYN"), Money(11), Money(12.01, "CNY")]
    s = sum(lst)
    print(s) #result in “BYN”
    #>>> 123.45 BYN
    # Exchange rate does not match
