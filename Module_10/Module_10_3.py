from random import randint
from threading import Lock
from threading import Thread
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.sync = Lock()
        self.deposite_finished = False

    def syncprint(self, *args):
        with self.sync:
            print(*args)

    def deposit(self):
        for i in range(100):
            topup = randint(50, 500)
            self.balance += topup
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.syncprint(f'Пополнение: {topup}. Баланс: {self.balance}')
            sleep(0.001)
        self.deposite_finished = True
        if self.lock.locked():
            self.lock.release()

    def take(self):
        i = 0
        while i < 100:
            if not self.lock.locked():
                withdrawal = randint(50, 500)
                self.syncprint(f'Запрос на {withdrawal}')
                if self.balance >= withdrawal:
                    self.balance -= withdrawal
                    self.syncprint(f'Снятие: {withdrawal}. Баланс: {self.balance}')
                else:
                    if not self.deposite_finished:
                        self.lock.acquire()
                    self.syncprint('Запрос отклонён, недостаточно средств')
                i += 1
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
