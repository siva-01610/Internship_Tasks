from solutions import (
    word_frequency, character_frequency, first_non_repeating_character,
    are_anagrams, first_repeating_character, move_zeros_to_end,
    second_highest_distinct, remove_duplicates_preserve_order,
    find_missing_number, first_pair_with_sum, closest_to_zero,
    common_elements, rotate_right, max_consecutive_sum,
    all_unique_pairs_with_sum
)

# Q1
print("Q1 Output:",word_frequency("python is easy and python is powerful"))
print("Q1 Output:", word_frequency("apple apple banana"))

# Q2
print("Q2 Output:", character_frequency("banana"))
print("Q2 Output:", character_frequency("hello"))

# Q3
print("Q3 Output:", first_non_repeating_character("swiss"))
print("Q3 Output:", first_non_repeating_character("hello"))

# Q4
print("Q4 Output:", are_anagrams("listen", "silent"))
print("Q4 Output:", are_anagrams("abc", "cab"))

# Q5
print("Q5 Output:", first_repeating_character("programming"))
print("Q5 Output:", first_repeating_character("abcdef"))

# Q6
print("Q6 Output:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Output:", move_zeros_to_end([1, 2, 3]))

# Q7
print("Q7 Output:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q7 Output:", second_highest_distinct([5, 5, 5]))

# Q8
print("Q8 Output:", remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Output:", remove_duplicates_preserve_order(["a", "b", "a", "c"]))

# Q9
print("Q9 Output:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Output:", find_missing_number([2, 3, 4, 5], 5))

# Q10
print("Q10 Output:", first_pair_with_sum([2, 7, 11, 15], 9))
print("Q10 Output:", first_pair_with_sum([3, 2, 4], 6))

# Q11
print("Q11 Output:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Output:", closest_to_zero([-5, 5, 2, -2]))

# Q12
print("Q12 Output:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Output:", common_elements(["a", "b", "c"], ["b", "c", "d"]))

# Q13
print("Q13 Output:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Output:", rotate_right([1, 2, 3], 5))

# Q14
print("Q14 Output:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Output:", max_consecutive_sum([-1, -2, -3, -4]))

# Q15
print("Q15 Output:", all_unique_pairs_with_sum([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Output:", all_unique_pairs_with_sum([2, 2, 3, 3, 4], 6))

