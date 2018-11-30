import math
import numpy as np


class Nakoplenie:
    def __init__(self, base_sum, period, procent, inflation, vnos):
        self.base_sum = base_sum
        self.period = period
        self.procent = procent
        self.inflation = inflation
        self.vnos = vnos

    def calc(self):
        for i in range(1, self.period):
            if i % 12 == 0 and i != 0:
                self.base_sum += self.vnos
            self.base_sum = self.base_sum * (1 + (self.procent - self.inflation) / 1200) - 31500
        return self.base_sum


class Ipoteka:
    def __init__(self, start_sum, price, proc, period_ipot, year_payment):
        self.start_sum = start_sum*10**6
        self.price = price*10**6
        self.proc = proc/100
        self.period = period_ipot * 12
        self.month_proc = self.proc / 12
        self.credit = self.price - self.start_sum
        self.year_payment = year_payment*10**6
        self.month = 0
        self.payments = []
        self.final_list = []

    def calc_payments(self):
        monthly_payment = self.credit * self.month_proc / (1 - (1 + self.month_proc)**(1-self.period))
        percent_payment = self.credit * self.month_proc
        body_payment = monthly_payment - percent_payment
        body_credit = self.credit
        for month in range(1, self.period):
            if body_credit > body_payment:
                if month % 12 == 0:
                    time = self.period - month
                    body_credit -= self.year_payment
                    self.payments.append([self.year_payment, 0, self.year_payment])
                    monthly_payment = body_credit * self.month_proc / (1 - (1 + self.month_proc)**(1-time))
                    if body_credit < self.year_payment:
                        monthly_payment = self.year_payment / 12
                percent_payment = body_credit * self.month_proc
                body_payment = monthly_payment - percent_payment
                body_credit = body_credit - body_payment
                self.payments.append([round(monthly_payment), round(percent_payment), round(body_payment, 2)])
            else:
                body_payment = body_credit
                body_credit -= body_payment
                monthly_payment = body_payment
                percent_payment = body_credit * self.month_proc
                if body_credit == 0:
                    self.month = month
                    self.payments.append([round(monthly_payment), round(percent_payment), round(body_payment, 2)])
                    break
            print(monthly_payment)
        return monthly_payment, percent_payment, body_payment, body_credit, self.month, self.payments

    def itogo(self):
        if self.month % 12 == 1:
            print('За ипотеку платить ' + str(self.month // 12) + ' лет и ' + str(
                self.month % 12) + ' месяц')
        elif self.month % 12 in range(0, 6):
            print('За ипотеку платить ' + str(self.month // 12) + ' лет и ' + str(
                self.month % 12) + ' месяца')
        else:
            print('За ипотеку платить ' + str(self.month // 12) + ' лет и ' + str(
                self.month % 12) + ' месяцев')

    def full_payment_during_period(self):
        # print(np.array(self.payments))
        self.final_list = np.sum(self.payments, axis=0)
        self.final_list = np.append([['Общая сумма платежей', 'Платежи по процентам', 'Платежи в тело кредита']], [self.final_list], axis=0)
        # print(self.final_list)
        return self.final_list


def compare(nakopl_sum, flat_price):
    diff = abs(nakopl_sum - flat_price)
    if nakopl_sum < flat_price:
        # print(ipotec_sum)
        print('Ипотека выгоднее, чем аренда жилья и накопления на ' + str(round(diff)))
    else:
        print('Ипотека говно, проигрывает при подобном заработке')

ipot = Ipoteka(1.2, 7.35, 8.9, 30, 1)
ipot.calc_payments()
ipot.full_payment_during_period()
ipot.itogo()
nakop = Nakoplenie(ipot.start_sum, ipot.month, 7, 4, ipot.year_payment)

print(ipot.full_payment_during_period())
print('За ' + str(nakop.period) + ' месяцев будет накоплено ' + str(round(nakop.calc())))

compare(nakop.base_sum, ipot.price)