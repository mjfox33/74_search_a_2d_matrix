class Solution:
    # simplest solution
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

    # uses binary search treating the 2d matrix as a 1d sorted list
    # this is accomplished by setting the right pointer to n*m-1
    # and translating the mid to row, col by row = mid // m, col = mid % m
    # and translating the final right pointer to row, col as above
    def searchMatrix2(self, matrix: list[list[int]], target:int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) # assuming all rows have the same number of columns
        pointer_left = 0 # matrix[0][0]
        pointer_right = n * m - 1 # matrix[n-1][m-1]
        while pointer_left != pointer_right:
            mid = (pointer_left + pointer_right - 1) // 2
            # convert mid to row, col
            # row = mid // m
            # col = mid % m
            if matrix[mid // m][mid %m] < target:
                pointer_left = mid + 1
            else:
                pointer_right = mid
        return matrix[pointer_right // m][pointer_right % m] == target
