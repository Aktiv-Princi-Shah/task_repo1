# - * - coding: utf - 8 -*-
def get_number_list():
    inp = input("Enter a series of numbers (comma-separated) as input: ")
    numbers = []
    for i in inp.split(","):
        i = i.strip()
        if i.isdigit():
            num = int(i)
            if num not in numbers:
                numbers.append(num)
    return numbers

def show_list(lst, msg):
    print(f"{msg}")
    for item in lst:
        print(item)

def filter_less_than_10(lst):
    return [i for i in lst if i > 10]

def filter_even(lst):
    return [i for i in lst if i % 2 == 0]

def filter_divisible_by_5(lst):
    return [i for i in lst if i % 5 == 0]

def show_stats(lst):
    if not lst:
        print('\nRemaining list is empty \nSo max number, min number, sum, Ascending-descending not possible')
    else:
        print('\nMax number = ', max(lst), '\nmin number = ', min(lst), '\nsum of total number = ', sum(lst))
        print('\nAscending order list = ', sorted(lst), '\ndescending order list = ', sorted(lst, reverse=True))

def show_types(original_list, list_2_tuple, list_2_set):
    print('\nCheck all types :')
    print(original_list, ' : ', type(original_list))
    print(list_2_tuple, ' : ', type(list_2_tuple))
    print(list_2_set, ' : ', type(list_2_set))

def pair_with_square(lst):
    print('\nList with its square:')
    for i in lst:
        print(f"{i} -> {i ** 2}")

def main():

    input_list = get_number_list()
    print("\nList of integers")
    show_list(input_list, "Input List:")

    original_list = input_list.copy()

    # From the list, remove all numbers less than 10.
    greater_than_ten_list = filter_less_than_10(input_list)
    print('\nLess than 10 list = ', greater_than_ten_list)

    # Check if all remaining numbers are even.
    even_list = filter_even(greater_than_ten_list)
    print('\nEven number: ', even_list)

    # Check if any of the remaining numbers are divisible by 5
    div_5_list = filter_divisible_by_5(greater_than_ten_list)
    print('\nDivisible 5 list: ', div_5_list)

    # Display the highest number, the lowest number, and the total of the remaining list.
    show_stats(greater_than_ten_list)

    # Convert the original list into a tuple and a set, and print both.
    list_2_tuple = tuple(original_list)
    list_2_set = set(original_list)
    print('\nList into tuple:', list_2_tuple, '\nlist into set:', list_2_set)

    # Print the type of all collections used and verify if each one belongs to its expected data type.
    show_types(original_list, list_2_tuple, list_2_set)

    # Pair each number in the original list with its square and display the result.
    pair_with_square(original_list)

main()
