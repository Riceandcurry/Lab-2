import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)




def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input()
    numbers = numbers.split(",")
    loop = 0
    for i in numbers:
        numbers[loop] = float(i)
        loop = loop + 1
    print(numbers)
    return numbers

def calc_average(num_list):
    total_list = 0
    no = 0
    for i in num_list:
        total_list = i + total_list
        no = no + 1
    average = total_list/no  #average
    print(average)
    return average

def find_min_max(num_list):
    max_temp = 0.0
    min_temp = 10000000.0
    for i in num_list:
        if i > max_temp:
            max_temp = i
        if i < min_temp:
            min_temp = i

    minmax_list = [min_temp, max_temp]
    return minmax_list

def sort_temperature(num_list):
    num_list.sort()
    print(num_list)

def calc_median_temperature(num_list):
    median = statistics.median(num_list)
    return median


if __name__ == "__main__":
    main()


