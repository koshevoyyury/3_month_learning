"""Practice Tasks
1. **Deduplicate with order preserved**
   * Input: `[1, 2, 2, 3, 4, 3]` → Output: `[1, 2, 3, 4]`
2. **Count characters in a string using dict**
3. **Write a function that returns the set of unique lowercase vowels in a string**
4. **Create a list of all keys in a dictionary where the value is greater than 10**"""

from typing import Dict, Set, List


def deduplicate_with_order(input_list: list) -> list:
    # fromkeys removes duplicates and keep order from python 3.7
    unique = list(dict.fromkeys(input_list))
    return unique


def count_char_in_string(input_str: str) -> Dict[str, int]:
    char_dict = {}
    for char in input_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def lower_case_vowels(input_str: str) -> Set[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return set(v for v in input_str.lower() if v in vowels)


def dict_keys_count(input_dict: Dict[str, int], val: int = 10) -> List[str]:
    return [k for k, v in input_dict.items() if v > val]


if __name__ == "__main__":
    # Task 1
    result = deduplicate_with_order(input_list=[1, 2, 2, 3, 4, 3])
    assert result == [1, 2, 3, 4]

    # Task 2
    result = count_char_in_string("alsdfaaaazagjf")
    assert result == {'a': 6, 'l': 1, 's': 1, 'd': 1, 'f': 2, 'z': 1, 'g': 1, 'j': 1}

    # Task 3
    result = lower_case_vowels("LSDJFLdksfjalsaaeeuuii")
    assert result == {'e', 'u', 'i', 'a'}

    # Task 4
    result = dict_keys_count({"first": 22, "second": 1, "third": 9})
    assert result == ["first"]
