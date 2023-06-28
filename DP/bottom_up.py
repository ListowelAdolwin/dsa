"""
Unlike in top-down approach, bottom-up tackles the smallest problems(starting from the base case) and uses those results to then tackle the bigger ones
"""

# Climbing Stairs
def climbStairs(n):
    memo = [0] * (n + 1)
    # The base cases (1 stair means 1 way to climb, 2 means 2 ways)
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

# House Robber
def houseRobber(nums):
    if len(nums) == 1:
        return nums[0]
    memo = [0] * (len(nums))
    memo[0] = nums[0]
    memo[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

    return memo[len(nums) - 1]


if __name__ == '__main__':
    print(climbStairs(20))
    print(houseRobber([8,9]))
