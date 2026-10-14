# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    result = {}

    for word in sentence.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    result = {}

    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    counts = character_frequency(word)

    for char in word:
        if counts[char] == 1:
            return char

    return 


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# Q5. Find the First Repeating Character in a String
def first_repeating_character(text):
    seen = []

    for char in text:
        if char in seen:
            return char
        else:
            seen.append(char)

    return 


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    for num in nums:
        if num == 0:
            result.append(num)

    return result


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)

    if len(unique_nums) >= 2:
        return unique_nums[1]
    else:
        return 


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    total = n * (n + 1) // 2
    present_total = sum(nums)

    return total - present_total


# Q10. Find Two Numbers Whose Sum Equals a Target
def first_pair_with_sum(nums, target):
    seen = []

    for num in nums:
        needed = target - num

        if needed in seen:
            return [needed, num]

        seen.append(num)

    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if len(nums) == 0:
        return 

    closest = nums[0]

    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if len(nums) == 0:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k != 0 else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    if len(nums) < 2:
        return 

    maximum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        total = nums[i] + nums[i + 1]

        if total > maximum:
            maximum = total

    return maximum


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs_with_sum(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort()

    return result
