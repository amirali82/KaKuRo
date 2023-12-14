class GameData:
    def __init__(self, fileUrl):
        file = open(fileUrl, 'r')

        self.n, self.m = file.readline().strip().split()
        self.n = int(self.n)
        self.m = int(self.m)

        self.UData = [[0] * self.m for _ in range(self.n)]
        self.LData = [[0] * self.m for _ in range(self.n)]
        self.isVarible = [[False] * self.m for _ in range(self.n)]
        self.value = [[0] * self.m for _ in range(self.n)]

        for i in range(self.n):
            line = file.readline()

            if not line:
                break

            row = line.strip().split(',')

            if row[-1] == "":
                row.pop()

            for j in range(self.m):
                c = row[j]
                c = c.strip()
                #print(c)
                if c == "b" or c == "w":
                    self.isVarible[i][j] = (c == "w")
                    self.UData[i][j] = -1
                    self.LData[i][j] = -1
                else:
                    c = c.strip("{}").split('/')
                    
                    if c[0] == "b":
                        self.LData[i][j] = -1
                    else:
                        self.LData[i][j] = int(c[0])
                    
                    if c[1] == "b":
                        self.UData[i][j] = -1
                    else:
                        self.UData[i][j] = int(c[1])

    def printSelf(self):
        print("N:", self.n, "M:", self.m)
        for i in range(self.n):
            for j in range (self.m):
                print("{", self.UData[i][j], self.LData[i][j], self.isVarible[i][j] ,  self.value[i][j],"}", end=" ")
            print()