'''
Task Description
Ask the user to enter a series of numbers (comma-separated) as input. ---
Convert this input into a list of integers. ---
From the list, remove all numbers less than 10. ---
Check if all remaining numbers are even.---
Check if any of the remaining numbers are divisible by 5.---
Display the highest number, the lowest number, and the total of the remaining list.---
Show the list sorted in both ascending and descending order.---
Convert the original list into a tuple and a set, and print both.---
Print the type of all collections used and verify if each one belongs to its expected data type.---
Pair each number in the original list with its square and display the result.
--------------------------------------------------------------------------------------------------'''
user_input = input("Enter Num: ")
original_list = user_input.split(',')
print("The comma sepeareted list : ",original_list)
print("--------------------------------------------")
filtered_list=[num for num in original_list if int(num) >= 10]
print("Values that are >= 10 are : ",filtered_list)
even_list=[num for num in filtered_list if int(num)%2 == 0]
print("The even list : ",even_list)
print("--------------------------------------------")
div_list=[num for num in even_list if int(num)%5 == 0]
print("The numbers those are divisible by 5 : ",div_list)
print("--------------------------------------------")
highest_list=max(div_list)
print("The highest among all is : ",highest_list)
lowest_list=min(div_list)
print("The lowest among all is : ",lowest_list)
remaining_elements = [int(x) for x in div_list if x != lowest_list and x != highest_list]
remain_li = [int(x) for x in remaining_elements]
remaining_elements = remain_li
print("The sum of the remaning elements of the list is: ",sum(remaining_elements))
print("--------------------------------------------")
ascending_list=remaing_elements.sort()
print("The ascending sorted list : ",ascending_list)
descending_list=remaing_elements.sort(reverse=True)
print("The descending sorted list: ",descending_list)
tuple_list=tuple(remaning_elements)
print("List to Tuple Conversion : ",tuple_list)
set_list=set(remaning_elements)
print("--------------------------------------------")
print("List to Set conversion : ",set_list)
print("original_list:", type(original_list))
print("filtered_list:", type(filtered_list))
print("tuple_list:", type(original_tuple))
print("set_list:", type(original_set))
print("--------------------------------------------")
squares = [(num, num ** 2) for num in original_list]
print("Original numbers with their squares: ")
for pair in squares:
    print(pair)

