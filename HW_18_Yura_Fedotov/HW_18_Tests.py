
import HW_18_Yura_Fedotov as test_api


def Test_WorkerHour():
    WorkerHourTest = test_api.WorkerHour(10, 1000, "Gregory")
    assert WorkerHourTest.surname == "Gregory"
    assert WorkerHourTest.salary == 8050.0
    return WorkerHourTest


def Test_WorkerFixed():
    WorkerFixedTest = test_api.WorkerFixed(10000, "James")
    assert WorkerFixedTest.surname == "James"
    assert WorkerFixedTest.salary == 8050.0
    return WorkerFixedTest


def Test_WorkerFOP():
    WorkerFOPTest = test_api.WorkerFOP(10, 1000, "Johnson")
    assert WorkerFOPTest.surname == "Johnson"
    assert WorkerFOPTest.salary == 9746.0
    return WorkerFOPTest


def Test_WorkerSelf():
    WorkerSelfTest = test_api.WorkerSelf(10, 1000, "Peterson")
    assert WorkerSelfTest.surname == "Peterson"
    assert WorkerSelfTest.salary == 7346.0
    return WorkerSelfTest

def Test_WorkerSelfA():
    WorkerSelfATest = test_api.WorkerSelf(10, 1000, "A")
    assert WorkerSelfATest.surname == "A"
    assert WorkerSelfATest.salary == 7346.0
    return WorkerSelfATest

def Test_WorkerSelfB():
    WorkerSelfBTest = test_api.WorkerSelf(10, 1000, "B")
    assert WorkerSelfBTest.surname == "B"
    assert WorkerSelfBTest.salary == 7346.0
    return WorkerSelfBTest


def Test_Sorting():
    assert (
        test_api.ItWorker.sort_workers(
            Test_WorkerFixed(),
            Test_WorkerHour(),
            Test_WorkerSelf(),
            Test_WorkerFOP(),
            Test_WorkerSelfA(),
            Test_WorkerSelfB()
        )
    ) == {
            'Johnson': 9746.0,
            'Gregory': 8050.0,
            'James': 8050.0,
            'A': 7346.0,
            'B': 7346.0,
            'Peterson': 7346.0
    }


if __name__ == '__main__':
    Test_Sorting()

