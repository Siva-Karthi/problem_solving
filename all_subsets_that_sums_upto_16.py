# This problem was asked by Google.
#
# Given a set of integers and a number k, find all the sub_sets that sum upto the given value k
#
# For example, given array = [10, 4, 2, 6] and k = 6
#
# [10,6]
# [10, 4, 2]
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time. You do not need to store the results. You can simply print them out as you compute them.

# descriptions:
# recursive problem
# specific datastructure?

# instant approach and mindset

# pseudocode:
# for i=0; i<=len of array; i++
#     for j = 0 ; j<len of array; j++
#       if i!=j:
#           sum = arr[i]+arr[j]
#

# The problem is to find all the subsets of a given set that add upto given number say 16
# noob answer find all the subsets of the given set then find the sum of each subset if sum is the given summ then print
# find the problem nature split the problem into subproblem and then find solution for each subproblems then merge

# Q: how to do the magic of subprobleming?
#  say here
import sys


def rec(arr, total, i):
    if total == 0:
        return 1
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr, total, i-1)
    else:
        return rec(arr, total-arr[i], i-1) + rec(arr, total, i-1)

def count_sets(arr, total):
    print(rec(arr, total, len(arr)-1))

arr = list(range(5))
tot = 6

count_sets(arr, tot)