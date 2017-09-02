

class mate:
    def __init__(self):
        self.num = 0
        self.elnum = 0
        self.lines = []

    def setNumEl(self,num,elnum):
        self.num=num
        self.elnum=elnum

    def setLine(self,num,line):
        while len(self.lines) < num:
            self.lines.append([])

        print str(len(self.lines))
        self.lines[num-1] = []
        for i in line:
            self.lines[num-1].append(i)

    def toFile(self,fileObj):
        fileObj.write("mate\n")
        temp = str(self.num) + ',' + str(self.elnum)
        fileObj.write(temp)
        fileObj.write("\n")

        for i in self.lines:
            temp = ''
            for j in i:
                temp = temp + str(j) + ','

            fileObj.write(temp)
            fileObj.write("\n")


        fileObj.write("\n\n")
