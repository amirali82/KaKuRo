from DataStruct import GameData

def solve_kauro(data):
    def isValid(data, r, c, num):

        rowSum = 0
        rowZeroCounter = 0

        pnt = c
        while (pnt < data.m and data.isVarible[r][pnt]):
            if (data.value[r][pnt] == num):
                return False
            rowSum += data.value[r][pnt]
            rowZeroCounter += (data.value[r][pnt] == 0)
            pnt += 1
        
        pnt = c - 1
        while (0 <= pnt and data.isVarible[r][pnt]):
            if (data.value[r][pnt] == num):
                return False
            rowSum += data.value[r][pnt]
            rowZeroCounter += (data.value[r][pnt] == 0)
            pnt -= 1

        
        if (rowZeroCounter == 1 and not (rowSum + num == data.UData[r][pnt])):
            return False
        if (rowSum + num > data.UData[r][pnt]):
            return False
        
        colSum = 0
        colZeroCounter = 0

        pnt = r
        while (pnt < data.n and data.isVarible[pnt][c]):
            if (data.value[pnt][c] == num):
                return False
            colSum += data.value[pnt][c]
            colZeroCounter += (data.value[pnt][c] == 0)
            pnt += 1
        
        pnt = r - 1
        while (0 <= pnt and data.isVarible[pnt][c]):
            if (data.value[pnt][c] == num):
                return False
            colSum += data.value[pnt][c]
            colZeroCounter += (data.value[pnt][c] == 0)
            pnt -= 1
        
        if (colZeroCounter == 1 and not (colSum + num == data.LData[pnt][c])):
            return False
        if (colSum + num > data.LData[pnt][c]):
            return False
        
        return True
    
    def solve(data):
        for i in range(data.n):
            for j in range(data.m):
                if (data.isVarible[i][j] and data.value[i][j] == 0):
                    for num in range(1, 10):
                        if isValid(data, i, j, num):
                            data.value[i][j] = num
                            if solve(data):
                                return True
                            data.value[i][j] = 0
                    return False

            #data.printSelf()
        return True
    
    res = solve(data)
    if res:
        print("Solved!")
    else:
        print("Not Solvable.")
    return data
        
