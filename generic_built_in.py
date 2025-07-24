def filter_list_num(original_list1):
    # From the list, remove all numbers less than 10.
    filtered_list = [num for num in original_list if num >= 10]
    print(f"\nValues that are >= 10 are : \n {filtered_list}")

    # Check if all remaining numbers are even.
    even_list = [num for num in filtered_list if num % 2 == 0]
    print(f"\nThe even list : \n {even_list}")
    
    #Check if any of the remaining numbers are divisible by 5.
    div_list = [num for num in even_list if num % 5 == 0]
    print(f"\nThe numbers those are divisible by 5 : \n {div_list}")

#Display the highest number, the lowest number, and the total of the remaining list.
def number_calculation(div_list):
    #The highest number
    highest_list=max(div_list)
    print(f"\nThe highest among all is : \n {highest_list}")

    #The lowest number
    lowest_list=min(div_list)
    print(f"\nThe lowest among all is : \n {lowest_list}")

    #The total of the remaining list
    remaining_elements = [int(x) for x in div_list if x != lowest_list and x != highest_list]
    remain_li = [int(x) for x in remaining_elements]
    remaining_elements = remain_li
    print(f"\nThe sum of the remaining elements of the list is: \n {sum(remaining_elements)}")

#Show the list sorted in both ascending and descending order.
def list_sorting(original_list):
    #Ascending Sort
    ascending_list = [int(i) for i in original_list]
    print()
    ascending_list.sort()
    print(f"\nThe ascending sorted list : \n {ascending_list}")

    #Descending Sort
    descending_list = [int(i) for i in original_list]
    print()
    descending_list.sort(reverse=True)
    print(f"\nThe descending sorted list: \n {descending_list}")

#Convert the original list into a tuple and a set, and print both.
def list_conversion(original_list1):
    tuple_list=tuple(original_list)
    print(f"\nList to Tuple Conversion : \n {tuple_list}")
    
    set_list=set(original_list)
    print(f"\nList to Set Conversion : \n {set_list}")
    
    #Print the type of all collections used and verify if each one belongs to its expected data type.
    print(f"\noriginal_list: {type(original_list)}")
    print(f"\ntuple_list: {type(tuple_list)}")
    print(f"\nset_list: {type(set_list)}")

#Pair each number in the original list with its square and display the result.
def finding_square(original_list1):
    squares = [(int(num), int(num)**2) for num in list(original_list)] 
    print(f"\nOriginal numbers {original_list} with their \nsquares: {squares}")

# Ask the user to enter a series of numbers (comma-separated) as input.
user_input = input("Enter comma separated list of numbers: ")
original_list = []
for item in user_input.split(','):
    item = item.strip()
    if item:
        try:
            original_list.append(int(item))
        except ValueError:
            print(f"Skipped invalid number: '{item}'")

print("The Numbers in a List:", original_list)

filter_list_num(original_list)
number_calculation(original_list)
list_sorting(original_list)
list_conversion(original_list)
finding_square(original_list)
