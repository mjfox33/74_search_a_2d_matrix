from code_74_search_a_2d_matrix import Solution

def test_example_1():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True

def test_example_2():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False