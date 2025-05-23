import Lab2

def test_min_max():
    result = []
    input_arr = [60, 40, 30, 20]
    test_arr = [20, 60]

    result = Lab2.find_min_max(input_arr)

    assert (result == test_arr)

def test_calc_average():
    result = []
    input_arr = [5, 67, 32, 50, 30]
    test_arr = 36.8

    result = Lab2.calc_average(input_arr)

    assert (result == test_arr)

def test_calc_median_temperature_even():
    result = []
    input_arr = [9.0, 16.0, 24.0, 30.0]
    test_arr = 20

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)

def test_calc_median_temperature_odd():
    result = []
    input_arr = [9.0, 16.0, 24.0, 30.0, 36.0]
    test_arr = 24

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)
