'''
In Top-down approach of Dynamic Programming, the biggest problem is tackled, which is then broken into smaller ones.
The solution of the smaller ones then give rise to that of the bigger one.

3 Steps to solve a DP problem;
i. A function and data structure; function to calculate each state of the dp and the data structure(hash map or array) to for memoization purposes
ii. A recurring relation; A recurring relation that relates one state of the dp to another.
ii. A base case; The base case stops the recursion.
'''

#1. Fibonacci Sequence
def fib(n):
    '''
    Find the nth fib number
    '''
    memo = {0:0, 1:1}
    def fibonnaci(num):
        if num in memo:
            return memo[num]
        memo[num] = fibonnaci(num - 1) + fibonnaci(num - 2)
        return memo[num]

    return fibonnaci(n)


#2. Climbing Stairs
def climbStairs(n):
    memo = {1:1, 2:2}
    def climb(num):
        if num not in memo:
            memo[num] = climb(num - 1) + climb(num - 2)
        return memo[num]

    return climb(n)

#3. House Robber
def houseRobber(houses):
    idx = len(houses) - 1
    memo = {0:houses[0], 1:max(houses[0], houses[1])}
    def rob(idx):
        if idx not in memo:
            memo[idx] = max(rob(idx - 1), rob(idx - 2) + houses[idx])
        return memo[idx]
    return rob(idx)

if __name__ == '__main__':
    print(fib(50))
    print(climbStairs(20))
    print(houseRobber([104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]))
