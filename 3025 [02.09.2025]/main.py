from solution import Solution

# points = [[2, 1], [6, 4], [2, 8], [4, 9], [8, 2], [7, 3]]
# points = [[1,1],[2,2],[3,3]]
# points = [[6,2],[4,4],[2,6]]
points = [[3,1],[1,3],[1,1]]

sol = Solution()
result = sol.numberOfPairs(points)

print(f"Количество подходящих пар: {result}")