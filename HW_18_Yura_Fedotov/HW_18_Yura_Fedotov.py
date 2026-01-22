import random

from abc import ABC, abstractmethod


class ItWorker(ABC):
    def __init__(self):
        self.salary = self.calculate_salary()
        self.WAR_TAX = 0.015
        self.PDFO = 0.18
        self.EP = 0.05
        self.ESV = 704
        self.calculate_tax()

    @abstractmethod
    def calculate_salary(self):
        return self.salary * 1

    @abstractmethod
    def calculate_tax(self):
        self.salary = self.salary - (
                self.PDFO * self.salary + self.WAR_TAX * self.salary
        )

    @staticmethod
    def sort_workers(*workers: object):
        return sorted(workers, key=lambda worker: worker.salary)


class WorkerHour(ItWorker):
    def __init__(self, hours:float, hour_salary:float):
        self.hours = hours
        self.hour_salary = hour_salary
        super().__init__()

    def calculate_salary(self):
        return self.hours * self.hour_salary

    def calculate_tax(self):
        super().calculate_tax()


class WorkerFixed(ItWorker):
    def __init__(self, fixed_salary: float):
        self.salary = fixed_salary
        super().__init__()

    def calculate_salary(self):
        return super().calculate_salary()

    def calculate_tax(self):
        super().calculate_tax()


class WorkerFOP(ItWorker):
    def __init__(self, hours: float, hour_salary: float):
        self.hours = hours
        self.hour_salary = hour_salary
        super().__init__()

    def calculate_salary(self):
        return self.hours * self.hour_salary * 1.1

    def calculate_tax(self):
        self.salary = self.salary - (
                self.EP * self.salary + self.ESV
        )

class WorkerSelf(ItWorker):
    def __init__(self, lines: float, lines_salary: float):
        self.lines = lines
        self.lines_salary = lines_salary
        super().__init__()

    def calculate_salary(self):
        return self.lines * self.lines_salary

    def calculate_tax(self):
        self.salary = self.salary - (
                self.PDFO * self.salary + self.WAR_TAX * self.salary + self.ESV
        )


if __name__ == '__main__':
    pass
