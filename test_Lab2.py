import pythonProject.Lab2 as lab2

def test_min_max():
    list = [23,67,34,1,6,45]
    correct_list = [1,67]
    result = lab2.find_min_max(list)
    assert (result == correct_list)

def test_average():
    correct_average = 45
    list = [30,50,20,40,60,70]
    result = lab2.calc_average(list)

    assert(result == correct_average)

def test_median_temperature():
    correct_median = 30
    list = [30,21,76,45,23]
    result = lab2.calc_median_temperature(list)

    assert (result == correct_median)