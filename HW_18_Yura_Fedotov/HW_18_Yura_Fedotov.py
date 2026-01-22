import random

from abc import ABC, abstractmethod


class ItWorker(ABC):
    def __init__(self, surname: str):
        self.surname = surname
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
        sorted_list = sorted(workers, key=lambda worker: (-worker.salary, worker.surname), reverse=False)
        sorted_dict = {}
        for worker_class in sorted_list:
            sorted_dict[worker_class.surname] = worker_class.salary
        return sorted_dict


class WorkerHour(ItWorker):
    def __init__(self, hours:float, hour_salary:float, surname:str):
        self.hours = hours
        self.hour_salary = hour_salary
        super().__init__(surname)

    def calculate_salary(self):
        return self.hours * self.hour_salary

    def calculate_tax(self):
        super().calculate_tax()


class WorkerFixed(ItWorker):
    def __init__(self, fixed_salary:float, surname:str):
        self.salary = fixed_salary
        super().__init__(surname)

    def calculate_salary(self):
        return super().calculate_salary()

    def calculate_tax(self):
        super().calculate_tax()


class WorkerFOP(ItWorker):
    def __init__(self, hours:float, hour_salary:float, surname:str):
        self.hours = hours
        self.hour_salary = hour_salary
        super().__init__(surname)

    def calculate_salary(self):
        return self.hours * self.hour_salary * 1.1

    def calculate_tax(self):
        self.salary = self.salary - (
                self.EP * self.salary + self.ESV
        )

class WorkerSelf(ItWorker):
    def __init__(self, lines:float, lines_salary:float, surname:str):
        self.lines = lines
        self.lines_salary = lines_salary
        super().__init__(surname)

    def calculate_salary(self):
        return self.lines * self.lines_salary

    def calculate_tax(self):
        self.salary = self.salary - (
                self.PDFO * self.salary + self.WAR_TAX * self.salary + self.ESV
        )


def generate_workers(num_of_workers:int):
    random_workers_list = []
    for i in range(num_of_workers):
        workers_class = random.choice([
            "WorkerHour", "WorkerFixed", "WorkerFOP", "WorkerSelf"
        ])
        worker_name = random.choice([
            "Smith", "Johnson", "Brown", "Taylor", "Anderson",
            "Thomas", "Jackson", "White", "Harris", "Martin",
            "Thompson", "Garcia", "Martinez", "Clark", "Lewis",
            "Walker", "Hall", "Allen", "Young", "King"
        ])
        match workers_class:
            case "WorkerHour": random_workers_list.append(
                WorkerHour(random.randint(120, 200), random.randint(50, 100), worker_name)
            )
            case "WorkerFixed": random_workers_list.append(
                WorkerFixed(random.randint(10000, 40000), worker_name)
            )
            case "WorkerFOP": random_workers_list.append(
                WorkerFOP(random.randint(120, 200), random.randint(50, 100), worker_name)
            )
            case "WorkerSelf": random_workers_list.append(
                WorkerFOP(random.randint(1000, 10000), random.randint(5, 10), worker_name)
            )
            case _:
                raise ValueError
    return random_workers_list


if __name__ == '__main__':
    print(ItWorker.sort_workers(*generate_workers(num_of_workers=10)))
