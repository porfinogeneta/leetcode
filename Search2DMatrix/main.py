def searchMatrix(matrix, target):
    # funkcja do znalezienia rzędu
    rows = len(matrix)
    # determine possible range for each number
    def rowRecu(l,r):
        if l > r:
            return -1
        mid = (l+r) // 2
        # jak znaleziony pierwszy element rzędu jest mniejszy od target
        if matrix[mid][0] <= target:
            if matrix[mid][-1] >= target: # kolejny rząd jest większy znaleźliśmy przedział
                return mid
            else:
                return rowRecu(mid+1,r) # badamy wyższy przedział

        elif matrix [mid][0] > target:
            return rowRecu(l,mid-1) # badamy niższy przedział
        elif matrix [mid][0] == target:
            return mid

    row = rowRecu(0, rows-1)
    if row == -1:
        return False
    toSearch = matrix[row]
    def binSearch(l,r):
        if l > r:
            return False
        mid = (l+r) // 2
        if toSearch[mid] > target:
            return binSearch(l,mid-1)
        elif toSearch[mid] < target:
            return binSearch(mid+1,r)
        elif toSearch[mid] == target:
            return True

    return binSearch(0, len(toSearch)-1)



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

print(searchMatrix(matrix, 60))