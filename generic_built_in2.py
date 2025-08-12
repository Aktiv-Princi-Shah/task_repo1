# - * - coding: utf - 8 -*-

def create_dictionary():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    scores_input = input("Enter scores (comma-separated integers): ")
    scores = [int(score.strip()) for score in scores_input.split(",") if score.strip().isdigit()]
    return {"name": name, "age": age, "scores": scores}

def apply_dict_methods(main_list):
    main_list1 = main_list.copy()
    print("new copy dictionary is: ",main_list1)
    print("\nApply All Dictionary Methods",main_list)

    # Demonstrating all major dictionary methods
    print("\nOriginal:", main_list1)
    print("\nget('name'):", main_list1.get("name"))
    print("\nkeys():", main_list1.keys())
    print("\nvalues():", main_list1.values())
    print("\nitems():", main_list1.items())
    print("\ncopy():", main_list1.copy())
    print("\npop('age'):", main_list1.pop("age"))
    print("\nAfter pop:", main_list1)
    main_list1["age"] = 25
    print("\nsetdefault('country', 'India'):", main_list1.setdefault("country", "India"))
    print("\nAfter setdefault:", main_list1)
    main_list1.update({"email": "princi@example.com"})
    print("\nAfter update():", main_list1)
    print("\npopitem():", main_list1.popitem())
    print("\nAfter popitem():", main_list1)
    print("\nfromkeys(['a','b'], 0):", dict.fromkeys(['a', 'b'], 0))
    main_list1.clear()
    print("\nAfter clear():", main_list1)

def evaluate_expression():
    # expr = input("\nEnter a mathematical expression (e.g., 2 + 3 * 4): ")
    result = eval(input("\nEnter a mathematical expression (e.g., 2 + 3 * 4): "))
    # result = eval(expr)
    print(f"\nEvaluated result: {result}")
    result_float = float(result)
    result_int = int(result)
    print(f"\nResult as float: {result_float}")
    print(f"\nResult as int: {result_int}")
    return result

def list_to_string_and_back(main_list):
    main_list_str1 = [str(num) for num in main_list]
    main_list_str = ", ".join(main_list_str1)

    print(f"\nList as string: {main_list_str}")
    main_list_back1 = eval(main_list_str)
    main_list_back = list(main_list_back1)
    print(f"\nString converted back to list: {main_list_back}")
    return main_list_back

def show_subset(main_list, start, end):
    subset = main_list[start:end]
    print(f"\nSubset of scores from index {start} to {end-1}: {subset}")
    return subset

def round_and_string(nums):
    print("\nRounded numbers as strings:")
    for num in nums:
        rounded = round(num)
        print(str(rounded))

def manual_first_three(main_list):
    print("\nFirst three scores (manual iteration):")
    count = 0
    for score in main_list:
        if count < 3:
            print(score)
            count += 1

def truthiness_tests():
    print("Truthiness tests:\n")
    print(f"\nEmpty list []: {bool([])}")
    print(f"\nNon-zero number 5: {bool(5)}")
    print(f"\nEmpty string '': {bool('')}")

def main():

    my_dict = create_dictionary()
    apply_dict_methods(my_dict)
    evaluate_expression()
    scores_list = my_dict["scores"]
    list_to_string_and_back(scores_list)
    show_subset(scores_list, 1, 4)
    round_and_string([1.2, 2.7, 3.5, 4.9])
    manual_first_three(scores_list)
    truthiness_tests()

main()
