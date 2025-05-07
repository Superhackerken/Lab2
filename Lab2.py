print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def main():
    display_main_menu()
    list_of_floats = get_user_input()
    average_value = calc_average(list_of_floats)
    min_max = find_min_max(list_of_floats)
    list_sorted = sort_temperature(list_of_floats)
    median = calc_median_temperature(list_sorted)
    print("User inputs: " + str(list_of_floats))
    print("Average of list: " + str(average_value))
    print("Min and max value: " + str(min_max))
    print("Sorted list: " + str(list_sorted))
    print("Median: " + str(median))
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
    print("calc_average_temperature")
    average = sum(floatlist) / len(floatlist)
    return average
def find_min_max(list):
    print("calc_min_max_temperature")
    maxi = max(list)
    mini = min(list)
    results = [mini, maxi]
    return results
def sort_temperature(list):
    print("sort_temperature")
    list.sort()
    return list
def calc_median_temperature(list):
    print("calc_median_temperature")
    if (len(list) % 2 == 0):
        #If true there is an even number of items in the list
        #List starts from 0, therefore minus 1
        return ((list[(len(list)//2)-1] + list[len(list)//2]) / 2)
    else:
        return list[int(len(list)//2)]

if __name__ == "__main__":

    main()
