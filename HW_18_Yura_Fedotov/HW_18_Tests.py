
import HW_18_Yura_Fedotov as test_api


def Test_WorkerHour():
    WorkerHourTest = test_api.WorkerHour(10, 1000, "Gregory")
    assert WorkerHourTest.surname == "Gregory"
    assert WorkerHourTest.salary == 8050.0


def Test_WorkerFixed():
    WorkerFixedTest = test_api.WorkerFixed(10000, "James")
    assert WorkerFixedTest.surname == "James"
    assert WorkerFixedTest.salary == 8050.0


def Test_WorkerFOP():
    WorkerFOPTest = test_api.WorkerFOP(10, 1000, "Johnson")
    assert WorkerFOPTest.surname == "Johnson"
    assert WorkerFOPTest.salary == 9746.0


def Test_WorkerSelf():
    WorkerFixedSelf = test_api.WorkerSelf(10, 1000, "Peterson")
    assert WorkerFixedSelf.surname == "Peterson"
    assert WorkerFixedSelf.salary == 7346.0

if __name__ == '__main__':
    Test_WorkerHour()
    Test_WorkerFixed()
    Test_WorkerFOP()
    Test_WorkerSelf()