#coding:utf-8
import sys
import datetime
import math
import  os
import homework1

if __name__ == '__main__':

    fileArr = []
    filepath = "./TestData"
    pathDir =  os.listdir(filepath)

    
    for allDir in pathDir:

        current_path = os.path.normpath(os.path.join(filepath, allDir))
        

        # print(os.path.abspath(os.path.join(dir, current_path)))
        print(os.path.normpath(os.path.join(filepath, allDir)))


        # child = os.path.join('%s%s' % (filepath, allDir))
        # print(child)
        fileArr.append(current_path)




    while True:
        print "The following are the TestData, input one index for the test, or input -1 to end."
        for i in range(len(fileArr)):
            print i,fileArr[i]
        ip = input('')
        if ip!=-1 :
            print "OK,file " + str(fileArr[ip]) + " is selected!"

            start = input('Please input a start point: ')
            end = input('Please input an end point: ')
            
            homework1.compute(fileArr[ip], start, end)



            
            
            print "\n"






        else:
            print "Algorithm ends!"
            sys.exit(0)


