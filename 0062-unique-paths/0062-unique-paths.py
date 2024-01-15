class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1]*n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
        
              
        
"""
def unique_paths(m, n):
    # Initialize a 2D array with all elements as 1. The array dimensions will be m x n.
    dp = [[1]*n for _ in range(m)]

    # Iterate through the array, starting from the cell (1,1), since the first row and first
    # column can only be reached in 1 way (all rights or all downs respectively).
    for i in range(1, m):
        for j in range(1, n):
            # The number of ways to reach a cell is equal to the sum of the number of ways
            # to reach the cell directly above it and the cell to the left of it.
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # The bottom-right corner will have the total number of unique paths.
    return dp[m-1][n-1]

# Example 1
m1, n1 = 3, 7
result1 = unique_paths(m1, n1)

# Example 2
m2, n2 = 3, 2
result2 = unique_paths(m2, n2)

print(result1)  # Output: 28
print(result2)  # Output: 3
"""