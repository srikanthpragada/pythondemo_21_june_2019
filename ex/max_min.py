# function returns a tuple with min and max values
def get_max_min(*nums):
    max_value = max(nums)
    min_value = min(nums)
    return (min_value, max_value)  # Create a tuple


large, small = get_max_min(10, 3, 43, 33, 2, 33, 444)  # Tuple unpacking

print(large, small)
