# Create a dictionary with keys: "name" (string), "age" (integer), and "scores" (list of integers).
def show_dict_operations():
    sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
    print("Dictionary Operations")
    print("Dictionary:", sample_dict)
    print("Available dictionary operations:")
    print(dir(sample_dict)) # Lists all methods and attributes

# Display all available operations or attributes that can be performed on this dictionary.
def apply_dict_methods():
    print("\nApply All Dictionary Methods")
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}

    # Demonstrating all major dictionary methods
    print("Original:", my_dict)
    print("get('name'):", my_dict.get("name"))
    print("keys():", my_dict.keys())
    print("values():", my_dict.values())
    print("items():", my_dict.items())
    print("copy():", my_dict.copy())
    print("pop('age'):", my_dict.pop("age"))
    print("After pop:", my_dict)
    my_dict["age"] = 25
    print("setdefault('country', 'USA'):", my_dict.setdefault("country", "USA"))
    print("After setdefault:", my_dict)
    my_dict.update({"email": "alice@example.com"})
    print("After update():", my_dict)
    print("popitem():", my_dict.popitem())
    print("After popitem():", my_dict)
    print("fromkeys(['a','b'], 0):", dict.fromkeys(['a', 'b'], 0))
    my_dict.clear()
    print("After clear():", my_dict)

# Ask the user to enter a mathematical expression as a string and evaluate its result.
def evaluate_expression():
    print("\nEvaluate Mathematical Expression")
    expression = input("Enter an expression (e.g., 5 + 3 * 2): ")
    try:
        result = eval(expression)
        print("Result:", result)
        print("As float:", float(result))
        print("As int:", int(result))
    except Exception as e:
        print("Invalid expression:", e)

# Convert the evaluated result into both float and integer types and print them.
def list_string_conversion():
    print("\nList to String and Back")
    my_list = ['apple', 'banana', 'cherry']
    list_str = ','.join(my_list)
    str_back = list_str.split(',')
    print("Original List:", my_list)
    print("List as String:", list_str)
    print("Back to List:", str_back)

# Convert a list into a string, and then convert it back to its original form.
def round_and_string():
    print("\nRounded and String Converted Values")
    rounded_strings = []
    for i in [1.2, 2.6, 3.5, 4.7]:
        r = round(i)
        s = str(r)
        rounded_strings.append(s)
        print(f"{i} -> {r} -> '{s}'")
# From the "scores" list, display a subset of elements using a range of indices.
def show_score_subset():
    print("\nSubset of Scores")
    scores = [45, 78, 88, 92, 67, 53, 81]
    subset = scores[2:5]
    print("Scores:", scores)
    print("Subset (index 2 to 4):", subset)

# Loop over a range of numbers, round each to the nearest whole number, and convert to string.
def round_numbers_to_string():
    rounded_numbers_dict = {}
    start_num = 1.2
    end_num = 5.8
    step = 0.7

    current_num = start_num
    index = 0
    while current_num <= end_num:
        rounded_num = round(current_num)
        rounded_num_str = str(rounded_num)
        rounded_numbers_dict[f"original_{current_num:.1f}"] = rounded_num_str
        current_num += step
        index += 1

    print(rounded_numbers_dict)

# Access the first three elements of the "scores" list using a manual iteration approach.
def manual_iteration():
    print("\nFirst 3 Elements (Manual)")
    scores = [45, 78, 88, 92, 67, 53, 81]
    i = 0
    while i < 3 and i < len(scores):
        print(scores[i])
        i += 1

# Test and display the truthiness of the following: an empty list, a non-zero number, and an empty string.
def test_truthiness():
    print("\nTruthiness Test")
    empty_list = []
    non_zero = 10
    empty_string = ""
    print("Empty list:", bool(empty_list)) # False
    print("Non-zero number:", bool(non_zero)) # True
    print("Empty string:", bool(empty_string)) # False

def main():
    show_dict_operations()
    apply_dict_methods()
    evaluate_expression()
    list_string_conversion()
    show_score_subset()
    round_and_string()
    round_numbers_to_string()
    manual_iteration()
    test_truthiness()

main()