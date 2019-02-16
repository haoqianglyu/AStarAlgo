#coding:utf-8
import sys
import datetime
import math
import os

def compute(file, startValue, endValue):

    starttime = datetime.datetime.now()
    saveedge = []
    savepoint = []




    file = open(file)
    data = file.readlines()
    verticesFlag = False
    edgesFlag = False
    for line in data:
        line = line.strip('\n')
        if line[0] == '#':
            continue
        if line[0] == 'V':
            verticesFlag = True
            continue
        if line[0] == 'E':
            edgesFlag = True
            verticesFlag = False
            continue
        if verticesFlag == True:
            odom = line.split(",", 3)  # split the data
            tmp = []
            tmp.append(int(odom[0]))
            tmp.append(int(odom[1]))
            tmp.append(int(odom[2]))
            savepoint.append(tmp)
        if edgesFlag == True:
            odom = line.split(",", 3)  # split the data
            tmp = []
            tmp.append(int(odom[0]))
            tmp.append(int(odom[1]))
            tmp.append(int(odom[2]))
            saveedge.append(tmp)



    class point:
        F = -1
        G = -1
        H = -1
        name = -1
        father = -1
        def __init__(self, a, b, c, d ,e):
            self.F = a
            self.G = b
            self.H = c
            self.name = d
            self.father = e

        def __str__(self):
            return '[' + str(self.F) + ',' + str(self.G) + ',' + str(self.H) + ',' + str(self.name) + ',' + str(self.father) + ']'



    beginpoint = startValue;
    endpointer = endValue;
    find = -1

    openpoint = [point(0, 0, 0, beginpoint, -1)]
    closepoint = []


    def change1():
        o1 = -1
        o2 = sys.maxint
        o3 = point(-1, -1, -1, 2, -1)
        for p in openpoint:
            if p.F < o2:
                o1 = p.name
                o2 = p.F
                o3 = p

        closepoint.append(o3)
        openpoint.remove(o3)
        return o1


    def findnear(f):
       tmp = []
       for p1 in saveedge:
           if p1[0] == f:
               ok = 1
               for p2 in closepoint:
                   if p2.name == p1[1]:
                       ok = -1
               if ok == 1:
                   tmp.append(p1[1])
               continue

           if p1[1] == f:
               ok = 1
               for p2 in closepoint:
                   if p2.name == p1[0]:
                       ok = -1
               if ok == 1:
                   tmp.append(p1[0])
               continue
       return tmp



    def change2(nowpoint = point(-1, -1, -1, -1, -1), pospoint = [1, 2]):
        for name in pospoint:
            inopen = -1;
            for p1 in openpoint:
                #found in openpoint
                if name == p1.name:
                    G = -1
                    for pp in saveedge:
                        if pp[0] == name and pp[1] == nowpoint.name:
                            G = nowpoint.G + pp[2]
                            break
                        if pp[1] == name and pp[0] == nowpoint.name:
                            G = nowpoint.G + pp[2]
                            break

                    H = int(math.sqrt(pow(savepoint[endpointer][1] - savepoint[name][1], 2) + pow(
                        savepoint[endpointer][2] - savepoint[name][2], 2)))

                    F = G + H
                    if F < p1.F:
                        p1.G = G
                        p1.H = H
                        p1.F = F
                        p1.father = nowpoint.name
                    inopen = 1
                    continue
            if inopen == 1:
                break;
            #openpoint don't have

            G = -1
            for pp in saveedge:
                if pp[0] == name and pp[1] == nowpoint.name:
                    G = nowpoint.G + pp[2]
                    break
                if pp[1] == name and pp[0] == nowpoint.name:
                    G = nowpoint.G + pp[2]
                    break

            H = int(math.sqrt(pow(savepoint[endpointer][1]-savepoint[name][1],2)+pow(savepoint[endpointer][2]-savepoint[name][2],2) ))

            F = G+H
            tmp = point(F, G, H, name, nowpoint.name)
            openpoint.append(tmp)


    def findpath():
        e33 = point(-1, -1, -1, 1, -1)
        for p in closepoint:
            if p.name == endpointer:
                return 1
        print e33
        return -1


    e33 = point(-1, -1, -1, 1, -1)
    def coutpath():

        
        for p in closepoint:
            if p.name == endpointer:
                e33 = p
                print "distance: " + str(e33.F)
                break
        path = ""

        p = e33
        while p.name != beginpoint:
            path += str(p.name) + "->"
            for point in closepoint:
                if point.name == p.father:
                    p = point
                    break
        path += str(beginpoint)

        print path





    while len(openpoint) or findpath() != 1:

        f1 = change1()
        f2 = findnear(f1)

        tmp1 = point(-1, -1, -1, -1, -1)
        for p in closepoint:
            if p.name == f1:
                tmp1 = p
                break

        f3 = change2(tmp1, f2)

    coutpath()
    endtime = datetime.datetime.now()
    print "runtime: " + str((endtime - starttime).seconds) + "s."
