'''
Task Description
Create a dictionary with keys: "name" (string), "age" (integer), and "scores" (list of integers).---
Display all available operations or attributes that can be performed on this dictionary.---
Ask the user to enter a mathematical expression as a string and evaluate its result.---
Convert the evaluated result into both float and integer types and print them.---
Convert a list into a string, and then convert it back to its original form.---
From the "scores" list, display a subset of elements using a range of indices.---
Loop over a range of numbers, round each to the nearest whole number, and convert to string.---
Access the first three elements of the "scores" list using a manual iteration approach.---
Test and display the truthiness of the following: an empty list, a non-zero number, and an empty string.---
-------------------------------------------------------------------------------------------------------'''
student={"Name":"Princi","Age":21,"Scores": [80,90,75,70,85]}
print(student)
expressions = input("Enter a Mathematical expression to perform: ")
try: 
    result = eval(expressions)
    print("Evaluated Result: ", result)
    print("------------------------------")
    float_result = float(result)
    int_result = int(result)
    print("As float: ",float_result)
    print("As int: ",int_result)
except Exception as e:
    print("Invalid expression:",e)
print("---------------------------------")
my_list=['stud1','stud2','stud3']
conversion_list=','.join(my_list)
print("The list converted to string : ",conversion_list)
back_list=conversion_list.split(',')
print("The string converted back to list : ",back_list)
print("---------------------------------")
scores_value = student['Scores'][:5]
print(scores_value)
start_index=2
end_index=5
subset = scores_value[start_index:end_index]
print("The set conversion of the scores value list is : ",subset)
print("--------------------------------------------------------")
rounded_string = []
for i in [1.2,2.6,3.5,4.7]:
    rounded_value = round(i)
    rounded_str=str(rounded_value)
    rounded_string.append(rounded_str)
    print("The conversion of whole num to string is : ",rounded_str)
print("--------------------------------------------------------")
i=0
while i<3 and i<len(scores_value):
    print(scores_value[i])
    i+=1
print("--------------------------------------------------------")
demo_list=[]
zero_val=10
empty_string=""
print("Empty List: ", bool(demo_list))
print("Non-zero Number: ", bool(zero_val))
print("Empty String: ", bool(empty_string))
print("--------------------------The End------------------------------")
