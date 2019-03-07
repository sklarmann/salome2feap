
import numpy


# Base Element class
class feapelem:

    def __init__(self):
        self.ids = []
        self.num = 0
        self.mat = 0
        self.ordered = False

    def getNum(self):
        return self.num

    def getMat(self):
        return self.mat

    def setNum(self, num):
        self.num = num

    def setMaterial(self, num):
        self.mat = num

    def addNodes(self, nodes):
        for i in nodes:
            self.ids.append(i)

    def numberOfNodes(self):
        return len(self.ids)

    def toFile(self, fileObj, numLines):
        s = str(self.num)
        fileObj.write(s)
        fileObj.write(',')
        s = str(self.mat)
        fileObj.write(s)
        fileObj.write(',')
        entry = 2
        cline = 1
        for i in self.ids:
            s = str(i)
            fileObj.write(s)
            fileObj.write(',')
            entry = entry + 1
            if entry >= 16:
                entry = 0
                cline = cline + 1
                fileObj.write('\n')

        while cline < numLines:
            fileObj.write('\n')
            cline = cline + 1

        fileObj.write('\n')


# 4 node Face Element
class feapelemQU4(feapelem):

    def setInitNodes(self, nodes):
        if len(nodes) != 4:
            print('Error when trying to add 9 node element')
        else:
            for i in range(4):
                self.ids.append(nodes[i])

    def reorder(self):
        tconn = []
        for i in self.ids:
            tconn.append(i)

        self.ids[0] = tconn[0]
        self.ids[1] = tconn[1]
        self.ids[2] = tconn[3]
        self.ids[3] = tconn[2]

    def reorderFeap(self):
        tconn = []


# 9 node Face Element
class feapelemQU9(feapelem):

    def setInitNodes(self, nodes):
        if len(nodes) != 9:
            print('Error when trying to add 9 node element')
        else:
            for i in range(9):
                self.ids.append(nodes[i])

    def reorder(self):
        tconn = []
        for i in self.ids:
            tconn.append(i)

        self.ids[0] = tconn[0]
        self.ids[1] = tconn[4]
        self.ids[2] = tconn[1]
        self.ids[3] = tconn[7]
        self.ids[4] = tconn[8]
        self.ids[5] = tconn[5]
        self.ids[6] = tconn[3]
        self.ids[7] = tconn[6]
        self.ids[8] = tconn[2]

    def reorderFeap(self):
        tconn = []


# 8 node Volume Element
class feapelemHE8(feapelem):
    def setInitNodes(self, nodes):
        if len(nodes) != 8:
            print('Error when trying to add 8 node element')
        else:
            for i in range(8):
                self.ids.append(nodes[i])

    def reorder(self):
        tconn = []
        for s in self.ids:
            tconn.append(s)

        self.ids[0] = tconn[0]
        self.ids[1] = tconn[3]
        self.ids[2] = tconn[1]
        self.ids[3] = tconn[2]
        self.ids[4] = tconn[4]
        self.ids[5] = tconn[7]
        self.ids[6] = tconn[5]
        self.ids[7] = tconn[6]


# 27 node Volume Element
class feapelemH27(feapelem):
    def setInitNodes(self, nodes):
        if len(nodes) != 27:
            print('Error when trying to add 27 node element')
        else:
            for i in range(27):
                self.ids.append(nodes[i])

    def reorder(self):
        tconn = []
        for s in self.ids:
            tconn.append(s)

        self.ids[0] = tconn[0]
        self.ids[1] = tconn[11]
        self.ids[2] = tconn[3]
        self.ids[3] = tconn[8]
        self.ids[4] = tconn[20]
        self.ids[5] = tconn[10]
        self.ids[6] = tconn[1]
        self.ids[7] = tconn[9]
        self.ids[8] = tconn[2]
        self.ids[9] = tconn[16]
        self.ids[10] = tconn[24]
        self.ids[11] = tconn[19]
        self.ids[12] = tconn[21]
        self.ids[13] = tconn[26]
        self.ids[14] = tconn[23]
        self.ids[15] = tconn[17]
        self.ids[16] = tconn[22]
        self.ids[17] = tconn[18]
        self.ids[18] = tconn[4]
        self.ids[19] = tconn[15]
        self.ids[20] = tconn[7]
        self.ids[21] = tconn[12]
        self.ids[22] = tconn[25]
        self.ids[23] = tconn[14]
        self.ids[24] = tconn[5]
        self.ids[25] = tconn[13]
        self.ids[26] = tconn[6]

    def reorientate(self, nodes, dire):
        # face 1
        node1 = nodes[self.ids[0]-1]
        node2 = nodes[self.ids[2]-1]
        node3 = nodes[self.ids[6]-1]

        x = [node2.xval()-node1.xval(), node2.yval()-node1.yval(),
             node2.zval()-node1.zval()]
        y = [node3.xval()-node1.xval(), node3.yval()-node1.yval(),
             node3.zval()-node1.zval()]

        dvec = numpy.cross(x, y)
        dlen = numpy.linalg.norm(dvec)
        if(abs(dvec[dire-1]) >= 0.9*dlen):
            # found
            print("found 1 nothin to do")
        else:
            # face 2
            node1 = nodes[self.ids[0]-1]
            node2 = nodes[self.ids[2]-1]
            node3 = nodes[self.ids[18]-1]

            # print node2.xval()
            x = [node2.xval()-node1.xval(), node2.yval()-node1.yval(),
                 node2.zval()-node1.zval()]
            y = [node3.xval()-node1.xval(), node3.yval()-node1.yval(),
                 node3.zval()-node1.zval()]

            dvec = numpy.cross(x, y)
            dlen = numpy.linalg.norm(dvec)
            if(abs(dvec[dire-1]) >= 0.9*dlen):
                print("found, reorder")
                node1 = nodes[self.ids[0]-1]
                node2 = nodes[self.ids[6]-1]
                tconn = []
                for s in self.ids:
                    tconn.append(s)
                if node1.xval() >= node2.xval():
                    for s in range(3):
                        self.ids[s+3] = tconn[s+9]
                        self.ids[s+6] = tconn[s+18]
                        self.ids[s+9] = tconn[s+3]
                        self.ids[s+12] = tconn[s+12]
                        self.ids[s+15] = tconn[s+21]
                        self.ids[s+18] = tconn[s+6]
                        self.ids[s+21] = tconn[s+15]
                        self.ids[s+24] = tconn[s+24]
