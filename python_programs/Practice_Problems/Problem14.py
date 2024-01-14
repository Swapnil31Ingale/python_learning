# # https://practice.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand0545/1?page=2&category[]=Mathematical&category[]=Numbers&category[]=number-theory&sortBy=submissions

# Calculate the angle between the hour hand and minute hand.

# Note: There can be two angles between hands; we need to print a minimum of 
# two. Also, we need to print the floor of the final result angle. 
# For example, if the final angle is 10.61, we need to print 10.

# Example 1:
# Input:
# H = 9 , M = 0
# Output:
# 90
# Explanation:
# The minimum angle between hour and minute
# hand when the time is 9 is 90 degress.

# Example 2:
# Input:
# H = 3 , M = 30
# Output:
# 75
# Explanation:
# The minimum angle between hour and minute
# hand when the time is 3:30 is 75 degress.

# Your Task:
# You don't need to read, input, or print anything. Your task is to complete 
# the function getAngle(), which takes 2 Integers H and M as input and returns
# the answer.

# Expected Time Complexity: O(1)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ H ≤ 12
# 0 ≤ M < 60
# H and M are Integers

def getAngle(H, M):
    # validate input
    if H < 1 or H > 12 or M < 0 or M >= 60:
        return -1  # invalid input
    
    # Calculate the angle formed by the hour hand with respect to 12:00
    hour_angle = 0.5 * (60 * H + M)

    # Calculate the angle formed by the minute hand with respect to 12:00
    minute_angle = 6 * M

    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Find the minimum angle (360 - angle) if it's greater than angle
    angle = min(360 - angle, angle)

    # Return the floor of the final result angle
    return int(angle)

# Example usage:
print(getAngle(9, 0))   # Output: 90
print(getAngle(3, 30))  # Output: 75

