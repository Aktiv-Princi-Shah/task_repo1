'''
def find_value_in_nested_dict(data, target_value):
    """
    Recursively searches for a target_value within a nested dictionary or list.

    Args:
        data: The nested dictionary or list to search.
        target_value: The value to find.

    Returns:
        True if the target_value is found, False otherwise.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if value == target_value:
                return True
            if isinstance(value, (dict, list)):
                if find_value_in_nested_dict(value, target_value):
                    return True
    elif isinstance(data, list):
        for item in data:
            if item == target_value:
                return True
            if isinstance(item, (dict, list)):
                if find_value_in_nested_dict(item, target_value):
                    return True
    return False

# Example Usage:
nested_dict = {
    'level1_key1': 'value1',
    'level1_key2': {
        'level2_key1': 'target_found',
        'level2_key2': [1, 2, {'level3_key': 'another_target'}]
    },
    'level1_key3': 'value3'
}

print(f"Is 'target_found' present? {find_value_in_nested_dict(nested_dict, 'target_found')}")
print(f"Is 'another_target' present? {find_value_in_nested_dict(nested_dict, 'another_target')}")
print(f"Is 'non_existent_value' present? {find_value_in_nested_dict(nested_dict, 'non_existent_value')}")'''

my_data = {'name': 'Alice', 'age': 30}
is_dict = isinstance(my_data, dict)
for key,value in my_data.items():
    if value == 30:
        print(my_data.value())
not_a_dict = [1, 2, 3]
is_not_dict = isinstance(not_a_dict, dict)
print(f"Is not_a_dict a dictionary? {is_not_dict}")
