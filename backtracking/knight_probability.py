class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def dp(x, y, n, visited, k):
            if k < 0:
                return 1
            if (x < 0 or x >= n) or (y < 0 or y >= n):
                return 0
            if (x, y, k) in visited:
                return visited[(x, y, k)]
            a = dp(x+2, y+1, n, visited, k-1)*1/8
            b = dp(x+2, y-1, n, visited, k-1)*1/8
            c = dp(x-2, y+1, n, visited, k-1)*1/8
            d = dp(x-2, y-1, n, visited, k-1)*1/8
            e = dp(x+1, y+2, n, visited, k-1)*1/8
            f = dp(x+1, y-2, n, visited, k-1)*1/8
            g = dp(x-1, y+2, n, visited, k-1)*1/8
            h = dp(x-1, y-2, n, visited, k-1)*1/8
            visited[(x, y, k)] = a + b + c + d + e + f + g + h
            return a + b + c + d + e + f + g + h
        return dp(row, column, n, {}, k)
