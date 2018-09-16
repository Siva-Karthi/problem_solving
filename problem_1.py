# This problem was asked by Google.
#
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

# assumptions:
# inputs are correct thats
# array contains only integers
# array length >= 1
# 1 <= k <= length of the array

# array = [10, 5, 2, 7, 8, 7]
# k = 3


# Questions:
# O(k) space ?

# descriptions:
# recursive problem
# specific datastructure?

# instant approach and mindset
# compute all the sub arrays of length k and get maximum of each

# 1)# related find all subsets os sets
    # filter given length
    # find max

# 2) solve using tree
#      dups are there


# k - number's sum = given sum

# pseudocode:
# for i=0; i<=len-k; i++
#     find the max of (array[i] , array[i+1],