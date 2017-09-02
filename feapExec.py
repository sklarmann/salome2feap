import h5py


from feap import *

def find_foo(name):
    print name

SalomeFile = "Mesh_1.med"
feapFile   = "ifeap2"

NumMaterial = 3
SpaceDim = 3
DofsPerNode = 3
NodesPerElement = 29

groupToMat = dict()
groupToMat[-6] = 1
groupToMat[-7] = 1
groupToMat[-8] = 2
groupToMat[-9] = 2
groupToMat[-10] = 3

f = h5py.File(SalomeFile, "r")

f.visit(find_foo)

Nodes = f['ENS_MAA/Mesh_1/-0000000000000000001-0000000000000000001/NOE']
Elems = f['ENS_MAA/Mesh_1/-0000000000000000001-0000000000000000001/MAI']


# print h[5]

test = feap()


test.addNodes(Nodes)
test.addElems(Elems)

test.setNumMat(NumMaterial)
test.setNdm(SpaceDim)
test.setNdf(DofsPerNode)
test.setNen(NodesPerElement)

test.GroupToMat(groupToMat)

test.addNodesToElementGroup(-10,[1,2])
test.addNodesToElementGroup(-8,[3,4])
test.addNodesToElementGroup(-9,[3,4])

#test.reorientateGroup(-10)

# OutPut Mesh to file
fileObj = open(feapFile,"w")
test.toFile(fileObj)
fileObj.close()

f.close()
