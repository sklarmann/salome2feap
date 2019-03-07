from feapnode import *
from feapelem import *
# import feapnode
# import feapelem


class feap:
    """docstring fs feap."""

    def __init__(self):
        self.elems = []
        self.nodes = []
        self.nummat = 0
        self.ndm = 0
        self.ndf = 0
        self.nen = 0

        self.groups = dict()
        self.mate = []
        self.cons = []
        self.boun = []
        self.macro = []
        self.load = []
        self.ebou = []
        self.solverparam = ''

    def addMate(self, mate):
        self.mate.append(mate)

    def setSolver(self, param):
        temp = 'solv\n'
        for i in param:
            temp = temp + str(i) + ','

        temp = temp + '\n'
        self.solverparam = temp

    def setEbou(self, dire, pos, blist):
        temp = []
        temp.append(dire)
        temp.append(pos)
        for i in blist:
            temp.append(i)

        self.ebou.append(temp)

    def addCons(self, cons, val):
        temp = cons + "=" + str(val)
        self.cons.append(temp)

    def addBoun(self, node, dofs):
        temp = str(node) + ','
        for i in dofs:
            temp = temp + ',' + str(i)

        self.boun.append(temp)

    def addLoad(self, num, dofs):
        temp = str(num) + ','
        for i in dofs:
            temp = temp + ',' + str(i)

        self.load.append(temp)

    def addMacroLine(self, line):
        self.macro.append(line)

    def addNodesSalome(self, Mesh):
        for i in range(Mesh.NbNodes()):
            coor = Mesh.GetNodeXYZ(i+1)
            self.nodes.append(feapnode(i+1, coor))

    def setMatGroupSalome(self, Group, Matnum):
        name = Group.GetName()
        if name not in self.groups:
            print('Error: Group does not exist')

        for i in self.groups[name]:
            self.elems[i-1].setMaterial(Matnum)

    def addNodesToElementGroupSalome(self, Group, Nodes):
        name = Group.GetName()

        if name not in self.groups:
            print('Error: Group does not exist')

        for i in self.groups[name]:
            self.elems[i-1].addNodes(Nodes)

        nn = self.elems[i-1].numberOfNodes()
        if nn > self.nen:
            self.nen = nn

    def reorder(self, Group, Ordering):
        name = Group.GetName()
        if Ordering == 'mult':
            for i in self.groups[name]:
                self.elems[i-1].reorder()
        elif Ordering == 'feap':
            for i in self.groups[name]:
                self.elems[i-1].reorderFeap()
        else:
            print('Error: Ordering Type unkown')

# Mesh, Group of Elements, SMESH.EntityType
    def addElemsSalome(self, Mesh, Group, Types):
        name = Group.GetName()
        elems = Group.GetIDs()
        print(name)
        if name not in self.groups:
            self.groups[name] = []

        for i in elems:
            eltype = Mesh.GetElementGeomType(i)
            if eltype == Types._item(18):  # Entity_TriQuad_Hexa
                if(self.nen < 27):
                    self.nen = 27
                elem = feapelemH27()
                nlist = Mesh.GetElemNodes(i)
                elem.setInitNodes(nlist)
                self.elems.append(elem)
                num = len(self.elems)
                elem.setNum(num)
                # elem.reorder()
                self.groups[name].append(num)
            elif eltype == Types._item(16):  # Entity_TriQuad_Hexa
                if(self.nen < 8):
                    self.nen = 8
                elem = feapelemHE8()
                nlist = Mesh.GetElemNodes(i)
                elem.setInitNodes(nlist)
                self.elems.append(elem)
                num = len(self.elems)
                elem.setNum(num)
                # elem.reorder()
                self.groups[name].append(num)
            elif eltype == Types._item(7):  # Entity_Quadrangle
                if(self.nen < 4):
                    self.nen = 4
                elem = feapelemQU4()
                nlist = Mesh.GetElemNodes(i)
                elem.setInitNodes(nlist)
                self.elems.append(elem)
                num = len(self.elems)
                elem.setNum(num)
                # elem.reorder()
                self.groups[name].append(num)
            elif eltype == Types._item(9):  # Entity_BiQuad_Quadrangle
                if(self.nen < 9):
                    self.nen = 9
                elem = feapelemQU9()
                nlist = Mesh.GetElemNodes(i)
                elem.setInitNodes(nlist)
                self.elems.append(elem)
                num = len(self.elems)
                elem.setNum(num)
                # elem.reorder()
                self.groups[name].append(num)

    def addNodes(self, nodes):
        # print nodes.keys()
        nums = nodes['NUM']
        coors = nodes['COO']
        nnodes = len(nums)
        x = []
        y = []
        z = []
        for i in range(nnodes):
            x.append(coors[i])
            y.append(coors[i+nnodes])
            z.append(coors[i+nnodes*2])

        for i in nums:
            temp = [x[i-1], y[i-1], z[i-1]]
            self.nodes.append(feapnode(i,temp))

    def addElems(self, elems):
        keys = elems.keys()
        for i in keys:
            if i == 'H27':
                data = elems[i]
                self.add27VolElement(data)
            elif i == 'HE8':
                data = elems[i]
                self.add8VolElement(data)
            elif i == 'QU9':
                data = elems[i]
                self.add9FaceElement(data)

    def GroupToMat(self, mapping):
        for i in mapping:
            if i in self.groups:
                num = mapping[i]
                for j in self.groups[i]:
                    #print j
                    self.elems[j-1].setMaterial(num)

    def reorientateGroup(self, group):
        for j in self.groups[group]:
            self.elems[j-1].reorientate(self.nodes, 1)

    def setNumMat(self, num):
        self.nummat = num

    def setNdm(self, ndm):
        self.ndm = ndm

    def setNdf(self, ndf):
        self.ndf = ndf

    def setNen(self, nen):
        self.nen = nen

    def numNodes(self):
        print(len(self.nodes))

    def printNodes(self):
        for i in self.nodes:
            i.printNode()

    def addNodesToElementGroup(self, group, nodes):
        for i in self.groups[group]:
            self.elems[i-1].addNodes(nodes)

    def toFile(self, fileObj):
        fileObj.write('feap\n')
        temp = str(len(self.nodes)) + ',' + str(len(self.elems)) + ',' \
            + str(self.nummat) + ',' + str(self.ndm) + ',' + str(self.ndf) \
            + ',' + str(self.nen)

        fileObj.write(temp)
        fileObj.write('\n\n')
        fileObj.write('coor\n')

        for i in self.nodes:
            i.toFile(fileObj)

        fileObj.write('\n\n')
        fileObj.write('elem\n')

        numLines = 1
        if self.nen > 13 and self.nen < 29:
            numLines = 2
        elif self.nen >= 29:
            numLines = 3
        for i in self.elems:
            i.toFile(fileObj, numLines)

        fileObj.write('\n\n')
        fileObj.write(self.solverparam)
        fileObj.write('\n\n')
        fileObj.write('cons\n')
        for i in self.cons:
            fileObj.write(i)
            fileObj.write('\n')

        fileObj.write('\n\n')

        for i in self.mate:
            i.toFile(fileObj)

        if len(self.boun) >= 1:
            fileObj.write('boun\n')
            for i in self.boun:
                fileObj.write(i)
                fileObj.write('\n')
            fileObj.write('\n\n')

        if len(self.load) >= 1:
            fileObj.write('load\n')
            for i in self.load:
                fileObj.write(i)
                fileObj.write('\n')
            fileObj.write('\n\n')

        if len(self.ebou) >= 1:
            fileObj.write('ebou\n')
            for i in self.ebou:
                for j in i:
                    fileObj.write(str(j))
                    fileObj.write(',')
                fileObj.write('\n')
            fileObj.write('\n\n')

        # fileObj.write('end\n\n\n')

        for i in self.macro:
            fileObj.write(i)
            fileObj.write('\n')

    def add27VolElement(self, data):
        nodes = data['NOD']
        group = data['FAM']
        pos = 0
        numels = len(group)
        for i in group:
            if i != 0:
                temp = feapelemH27()
                ids = []
                for j in range(27):
                    ids.append(nodes[pos + numels*j])

                temp.setInitNodes(ids)
                self.elems.append(temp)
                num = len(self.elems)
                temp.setNum(num)
                temp.reorder()
                temp.setMaterial(i)

                if i not in self.groups:
                    self.groups[i] = []

                self.groups[i].append(num)

            pos = pos + 1

    def add8VolElement(self, data):
        nodes = data['NOD']
        group = data['FAM']

        pos = 0
        numels = len(group)
        for i in group:
            if i != 0:
                temp = feapelemHE8()
                ids = []
                for j in range(8):
                    ids.append(nodes[pos+numels*j])

                temp.setInitNodes(ids)
                self.elems.append(temp)
                num = len(self.elems)
                temp.setNum(num)
                temp.reorder()
                temp.setMaterial(i)

                if i not in self.groups:
                    self.groups[i] = []

                self.groups[i].append(num)

            pos = pos + 1

    def add9FaceElement(self, data):
        nodes = data['NOD']
        group = data['FAM']

        pos = 0
        numels = len(group)
        for i in group:
            if i != 0:
                temp = feapelemQU9()
                ids = []
                for j in range(9):
                    ids.append(nodes[pos+numels*j])

                temp.setInitNodes(ids)
                self.elems.append(temp)
                num = len(self.elems)
                temp.setNum(num)
                temp.reorder()
                temp.setMaterial(i)
                if i not in self.groups:
                    self.groups[i] = []

                self.groups[i].append(num)

            pos = pos + 1
