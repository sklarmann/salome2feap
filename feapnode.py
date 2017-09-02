# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:34:54 2017

@author: Klarmann
"""

class feapnode:
    """docstring for node."""

    def __init__(self, num, inputS):
        self.num = num
        self.coor = inputS
        # for i in range(3):
        #     self.coor.append(inputS[i])


    def toString(self):
        temp = str(self.num) + ','
        for i in self.coor:
            s = "{:.10E}".format(i)
            temp = temp + ',' + str(s)
        return temp

    def printNode(self):
        print self.toString()

    def toFile(self,fileObj):
        fileObj.write(self.toString())
        fileObj.write("\n")

    def xval(self):
        return self.coor[0]
    
    def yval(self):
        return self.coor[1]
    
    def zval(self):
        return self.coor[2]