# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odd_nums = [el for el in source_array if el %2 != 0]
    odd_nums.sort()
    idx = 0
    for i, num in enumerate(source_array):
        if num %2 != 0:
            source_array[i] = odd_nums[idx]
            idx += 1
    return source_array