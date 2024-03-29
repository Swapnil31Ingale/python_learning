# # https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1?page=3&category[]=Mathematical&category[]=Numbers&category[]=number-theory&sortBy=submissions

# # Given two rectangles, find if the given two rectangles overlap or not. 
# A rectangle is denoted by providing the x and y coordinates of 
# two points: the left top corner and the right bottom corner of the 
# rectangle. Two rectangles sharing a side are considered overlapping. 
# (L1 and R1 are the extreme points of the first rectangle and L2 and R2 
# are the extreme points of the second rectangle).

# Note: It may be assumed that the rectangles are parallel to the 
# coordinate axis.

# rectanglesOverlap

# Example 1:

# Input:
# L1=(0,10)
# R1=(10,0)
# L2=(5,5)
# R2=(15,0)
# Output:
# 1
# Explanation:
# The rectangles overlap.
# Example 2:

# Input:
# L1=(0,2)
# R1=(1,1)
# L2=(-2,0)
# R2=(0,-3)
# Output:
# 0
# Explanation:
# The rectangles do not overlap.

# Your Task:
# You don't need to read input or print anything. Your task is to complete
# the function doOverlap() which takes the points L1, R1, L2, and R2 as 
# input parameters and returns 1 if the rectangles overlap. Otherwise, 
# it returns 0.


# Expected Time Complexity:O(1)
# Expected Auxillary Space:O(1)


# Constraints:
# -109<=x-coordinate,y-coordinate<=109

def doOverlap(L1, R1, L2, R2):
    # If one rectangle is to the left of the other
    if R1[0] < L2[0] or R2[0] < L1[0]:
        return 0  # No overlap

    # If one rectangle is above the other
    if R1[1] > L2[1] or R2[1] > L1[1]:
        return 0  # No overlap

    # Rectangles overlap
    return 1

# Example usage:
result1 = doOverlap((0, 10), (10, 0), (5, 5), (15, 0))
result2 = doOverlap((0, 2), (1, 1), (-2, 0), (0, -3))

print(result1)  # Output: 1 (Overlap)
print(result2)  # Output: 0 (No overlap)



# Rectangle 1
# (0,10)--------(10,10)
#  |             |
#  |             |
#  |             |
# (0,0)--------- (10,0)

# Rectangle 2
# (5,5)---------(15,5)
#  |             |
#  |             |
#  |             |
# (5,0)--------- (15,0)



# Rectangle 1
# (0,2)---------(1,2)
#  |            |
#  |            |
#  |            |
# (0,0)--------- (1,0)

# Rectangle 2
# (-2,0)---------(0,0)
#  |            |
#  |            |
#  |            |
# (-2,-3)------- (0,-3)
