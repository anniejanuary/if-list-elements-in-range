# Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range.
# 
# Example 1:
# 
# Input: N = 7, A = 2, B = 5
# arr[] =  {1, 4, 5, 2, 7, 8, 3}
# Output: Yes
# Explanation: It has elements between 
# range 2-5 i.e 2,3,4,5


class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        range1 = range(A, B)
        for i in arr:
            if i in range1:
                str1 = "In range"
                return str1
            else:
                str2 = "Not in range"
                return str2
