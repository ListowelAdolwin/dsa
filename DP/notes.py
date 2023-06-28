'''Dynamic Programming (DP) is a programming paradigm that can systematically and efficiently explore all possible solutions to a problem. As such, it is capable of solving a wide variety of problems that often have the following characteristics:

The problem can be broken down into "overlapping subproblems" - smaller versions of the original problem that are re-used multiple times.
The problem has an "optimal substructure" - an optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem.
As a beginner, these theoretical definitions may be hard to wrap your head around. Don't worry though - at the end of this chapter, we'll talk about how to practically spot when DP is applicable. For now, let's look a little deeper at both characteristics.

The Fibonacci sequence is a classic example used to explain DP. For those who are unfamiliar with the Fibonacci sequence, it is a sequence of numbers that starts with 0, 1, and each subsequent number is obtained by adding the previous two numbers together.

If you wanted to find the nth Fibonacci number F(n), you can break it down into smaller subproblems - find F(n - 1) and F(n - 2) instead. Then, adding the solutions to these subproblems together gives the answer to the original question, F(n - 1)+F(n - 2)=F(n), which means the problem has optimal substructure, since a solution F(n) to the original problem can be formed from the solutions to the subproblems. These subproblems are also overlapping - for example, we would need F(4) to calculate both F(5) and F(6).

These attributes may seem familiar to you. Greedy problems have optimal substructure, but not overlapping subproblems. Divide and conquer algorithms break a problem into subproblems, but these subproblems are not overlapping (which is why DP and divide and conquer are commonly mistaken for one another).

Dynamic programming is a powerful tool because it can break a complex problem into manageable subproblems, avoid unnecessary recalculation of overlapping subproblems, and use the results of those subproblems to solve the initial complex problem. DP not only aids us in solving complex problems, but it also greatly improves the time complexity compared to brute force solutions. For example, the brute force solution for calculating the Fibonacci sequence has exponential time complexity, while the dynamic programming solution will have linear time complexity because it reuses the results of subproblems rather than recalculating the results for previously seen subproblems. The difference in work required by the brute force approach compared to the dynamic programming approach is visually demonstrated on the next page.

Throughout this explore card, you will gain a better understanding of what makes DP so powerful. In the next section, we'll discuss the two main methods of implementing a DP algorithm.
'''

def fib(n):
    '''
    Find the nth fibonacci number
    Without DP, this problem can be solved as follows(with 2^n time complexity)
    Meanwhile with DP, this could be solved with just o(n)
    '''
    print(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(50))
