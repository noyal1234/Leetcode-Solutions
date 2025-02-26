class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        while matrix:
            a += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    a.append(row.pop())
            if matrix:
                a+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    a.append(row.pop(0))
        return a

