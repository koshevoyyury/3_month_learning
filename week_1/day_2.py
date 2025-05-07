"""Practice Tasks"""
from typing import List


# 1. **Write a function that receives a tuple of numbers and returns the sum of even numbers.
def sum_even(tpl):
    return sum(n for n in tpl if n % 2 == 0)


# 2. **Swap two values using tuple unpacking. Try it with three variables too.
def swap_values():
    k, v = (2, 3)
    print(f"First value: {k}")
    print(f"Second value: {v}")

    x, y, z = (1, 2, 3)
    print(f"X: {x}")
    print(f"Y: {y}")
    print(f"Z: {z}")


# 3. **Try changing a value inside a tuple and explain the error.
def value_change_error():
    t = (1, 2, 3)
    try:
        t[0] = 99  # TypeError
    except TypeError as ex:
        print(f"We can't change tuple value since it is immutable. So, we got TypeError exception: {ex}")


# 4. **Write a function that returns the second-to-last element from any sequence (list, tuple, string).
def second_last(seq):
    return seq[1:]


# Leet code 1365
def count_nums(nums: List[int]) -> List[int]:
    """
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    """
    sorted_nums = sorted(nums)
    count_dict = {}

    for i, n in enumerate(sorted_nums):
        if n not in count_dict:
            count_dict[n] = i

    return [count_dict[num] for num in nums]


if __name__ == "__main__":
    assert sum_even((2, 3, 4)) == 6

    swap_values()

    value_change_error()

    assert (2, 3, 6, 8) == second_last((1, 2, 3, 6, 8))

    assert [4, 0, 1, 1, 3] == count_nums([8, 1, 2, 2, 3])
