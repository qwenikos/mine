#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "run as main program"
def readDataFromFileToDict(filename,rankThreshold,refereneceColumn):
    f = open(filename, 'r')
    dataDict={}
    goon=True
    count=0
    linesNum=f.readline()
    print linesNum
    linesNum=linesNum.rstrip().split("\t")[1]
    columnsNum=f.readline()
    print columnsNum
    columnsNum=columnsNum.rstrip().split("\t")[1]
    i=0
    for line in f:
#        print "loop "+str(i)
        i+=1
        cols=line.rstrip().split("\t")
        compoundName=cols[0]
        smileStr=cols[1]
        
        dataDict[cols[0]]=[]
        firsrColumn=2
        lastColumn=int(columnsNum)+1
        refColumn=refereneceColumn+1 #efoson xekinan sto 2 
        count=0
#        print i
        for j in range(firsrColumn,lastColumn+1): #gia kathe compound ypologise th diafora
#            print "cols[j]="+str(cols[j])
#            print "cols[refColumn]= "+str(cols[refColumn])
            if cols[j]=="": #an den yphrxe toy dinw  0 poy einai poly megalo
                cols[j]=0
            if cols[refColumn]=="": #an den yphrxe toy dinw  0 poy einai poly megalo
                cols[refColumn]=0
            difftoRef=float(cols[j])-float(cols[refColumn])
#            print"difftoRef="+str(difftoRef)
            if difftoRef>rankThreshold:
                count+=1
        
        if (count ==int(columnsNum)-1): #an se ola h diafora einai megalyterh apo to threshold
            print line
            
            
        
        
        if i==20000:
            break  
    return

#this is the main program
filename= "output_2016-01-24_00_59_02.dat"
rankThreshold=2
energyThreshold=1
refereneceColumn=2#the numbering start at 3
readDataFromFileToDict(filename,rankThreshold,refereneceColumn)
