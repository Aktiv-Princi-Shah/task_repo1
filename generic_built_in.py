'''
Convert the original list into a tuple and a set, and print both.'''
'''
Ask the user to enter a series of numbers (comma-separated) as input and Convert this input into a list of integers.

split() -> Converts the entered comma separated value into list

Returns:
list of number in list formate
'''

user_input = input("Enter Num: ")
original_list = user_input.split(',')
print(f"\nThe comma separated list : \n {original_list}")

'''
From the list, remove all numbers less than 10, Check if all remaining numbers are even and Check if any of the remaining numbers are divisible by 5.

Parameters:
-num -> fetches individual numbers/digits from the list

Returns:
- list of numbers those are greater than or equal to 10
- sorted list of numbers that are even
- sorted list of numbers those are divisible by 5
'''

filtered_list=[num for num in original_list if int(num) >= 10]
print(f"\nValues that are >= 10 are : \n {filtered_list}")

even_list=[num for num in filtered_list if int(num)%2 == 0]
print(f"\nThe even list : \n {even_list})

div_list=[num for num in even_list if int(num)%5 == 0]
print(f"\nThe numbers those are divisible by 5 : \n {div_list}")

'''
Display the highest number, the lowest number, and the total of the remaining list and Show the list sorted in both ascending and descending order.

Parameters:
-max -> helps find the maximum number
-min -> helps find the minimum number
-sum -> helps perform the addition of the numbers passed
- sort -> sorts the given list in ascending order by default
- reverse=True inside sort to get the descending order of the list values.

Returns:
- highest number
- lowest number
- sum of the present in the list 
- sorted list
'''

highest_list=max(div_list)
print(f"\nThe highest among all is : \n {highest_list}")
lowest_list=min(div_list)
print(f"\nThe lowest among all is : \n {lowest_list}")
remaining_elements = [int(x) for x in div_list if x != lowest_list and x != highest_list]
remain_li = [int(x) for x in remaining_elements]
remaining_elements = remain_li
print(f"\nThe sum of the remaining elements of the list is: \n {sum(remaining_elements)}")
ascending_list=remaining_elements.sort()
print(f"\nThe ascending sorted list : \n {ascending_list}")
descending_list=remaining_elements.sort(reverse=True)
print(f"\nThe descending sorted list: \n {descending_list}")

'''
- Convert the original list into a tuple and a set, and print both.
- Print the type of all collections used and verify if each one belongs to its expected data type.

Parameter: 
- tuple() -> to type cast the list into tuple.
- set() -> to type cast into set.
- type() -> to identify the type of given inputs.

Returns:
- tupled list, set and prints each type name of the present type of data.
'''

tuple_list=tuple(remaining_elements)
print(f"\nList to Tuple Conversion : \n {tuple_list}")
set_list=set(remaining_elements)
print(f"\nList to Set Conversion : \n {set_list}")

print(f"\noriginal_list: {type(original_list)}")
print(f"\nfiltered_list: {type(filtered_list)}")
print(f"\ntuple_list: {type(tuple_list)}")
print(f"\nset_list: {type(set_list)}")

'''
Pair each number in the original list with its square and display the result.

Parameters:
- ** -> to calculate the power of the number
- list to iterate the list to find the power of each number in the list.

Returns:
- list of power of the numbers.
'''

squares = [(int(num), int(num)**2) for num in list(original_list)] 
print(f"\nOriginal numbers {original_list} with their squares: {squares}")

