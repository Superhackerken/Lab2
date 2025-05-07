print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    print("get_user_input")
    user_input = input()
    input_split = user_input.split(",")
    float_list = [float(item) for item in input_split]
    return float_list
def calc_average(floatlist):
    print("calc_average")
    average = sum(floatlist) / len(floatlist)
    return average
def find_min_max(list):
    print("find_min_max")
    maxi = max(list)
    mini = min(list)
    results = [mini, maxi]
    return results
def sort_temperature(list):
    print("sort_temperature")
    list.sort()
    print(list)
def calc_median_temperature():
    print("calc_median_temperature")

display_main_menu()
list_of_floats = get_user_input()
average_value = calc_average(list_of_floats)
min_max = find_min_max(list_of_floats)