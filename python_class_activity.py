# -*- coding: utf-8 -*-
"""Python Class activity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-HBdF3bmfdIt_PTmDpKJ1m99DU5JDORe
"""

# Question 1: Find largest difference

def largest_difference(numbers):
    min_val = float('inf')
    max_diff = 0
    for num in numbers:
        if num < min_val:
            min_val = num
        else:
            max_diff = max(max_diff, num - min_val)
    return max_diff

print(largest_difference([1, 2, 90, 10, 110]))

# Question 2: First non repeating character

def first_non_repeating(characters):
    for i in characters:
        if characters.count(i) == 1:
            return i
    return None
print(first_non_repeating("aabcc"))

# Question 3: Check Permutations:

def are_permutations(a, b):
    if len(a) != len(b):
        return False
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if sorted_a == sorted_b:
        return True
    else:
        return False

print(are_permutations("abc", "bca"))

#Question 4: Second Largest Unique Number:

def second_largest_unique(nums):

    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    uniques = [num for num in counts if counts[num] == 1]

    if len(uniques) < 2:
        return None

    uniques.sort(reverse=True)
    return uniques[1]

print(second_largest_unique([4, 5, 6, 6, 7]))

# Question 5: Count distinct Pairs

def count_distinct_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return len(pairs)

print(count_distinct_pairs([1, 2, 3, 4, 3, 6], 6))

#Question 6: Remove Duplicates from list:

def remove_duplicates(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 5, 1]))

# Question 7: Subset of list

def sub_sets(lst):
    subsets = [[]]
    for num in lst:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
        subsets.extend(new_subsets)
    return subsets

# Example
print(sub_sets([1, 2, 3]))

# Question 8: Longest increasing Sequence:

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))

# Question 9: Max product

def max_product(nums):
    nums.sort()
    return max(nums[0]*nums[1], nums[-1]*nums[-2])

print(max_product([1, 10, -5, 1, 100]))

# Question 10: Most frequency of the character

def most_frequent_char(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    max_freq = max(freq.values())

    candidates = [char for char in freq if freq[char] == max_freq]

    return min(candidates)

print(most_frequent_char("aabbbc"))

# Question 11: Print lower number:

def num_less_than_n(n):
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

# Example
print(num_less_than_n(10))

