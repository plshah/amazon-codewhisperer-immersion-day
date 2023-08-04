# Create a function for binary search
def binary_search_recursive(list, item):
    if len(list) == 0:
        return None
    else:
        mid = len(list) // 2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            return binary_search_recursive(list[:mid], item)
        else:
            return binary_search_recursive(list[mid + 1:], item)