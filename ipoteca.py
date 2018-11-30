class Nakoplenie:

    def __init__(self, period, flat_price, init_fee, int_rate): #int_rate - ставка
        self.period = period
        self.flat_price = flat_price
        self.init_fee = init_fee
        self.int_rate = int_rate


    def calc(self):
        credit = self.flat_price - self.init_fee
        for i in range(self.period):
            credit *= (1+self.int_rate/100)
        return credit


my_nak = Nakoplenie(30, 3000000, 1500000, 7)
print(my_nak.calc())

