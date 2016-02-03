# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import os.path
from collections import OrderedDict
##-------------------------------------------
def createFileList(linux):
    windowsPathPrefix="/biothesis/" 
    linuxPathPrefix="/home/nikos/biothesis/"
    filename1="data/Human/ChIPseq/Pol2/ESC/GSM822300/macs/Pol2_peaks.bed"
    filename2="data/Human/ChIPseq/H3K4me3/ESC/GSM605315/sicer/w200_g400/accepted_hits_noDupl-W200-G400.scoreisland"
    inputfileList=[filename1,filename2]
    outputFileList=[]
    for fl in inputfileList:
        if linux==0: ##an se windows   
            fl=windowsPathPrefix+fl      
        else:
            fl=linuxPathPrefix+fl
        fl=os.path.abspath(fl) ##if start ith / then absolut else relative path
        outputFileList+=[fl]
#    print inputfileList
#    print"\n"
#    print outputFileList
    return outputFileList
    
def readData(filename,chomCol,fStartCol,fEndCol):
    print "reading "+filename
    ##filename the datafile filename
    ##chomCol the column with chrom name
    ##fStartCol the column with feature Start Pos
    ##fEndCol the column with feature End Pos
    dataList=[] #store fileData
    dataPerChromDict={}
    cols=[]
    baseFileName=os.path.basename(filename)
#    print baseFileName
    chomCol=int(chomCol)-1
    fStartCol=int(fStartCol)-1
    fEndCol=int(fEndCol)-1
    f = open(filename, 'r')
    goon=True
    count=1
    for line in f:
        cols=line.rstrip().split("\t")
        fChrom=cols[chomCol]
        fStartPos=cols[fStartCol]
        fEndPos=cols[fEndCol]
        fLength=int(fEndPos)-int(fStartPos)
        if goon:
            dataList.append([count,fChrom,fStartPos,fEndPos,baseFileName])
            count+=1;
#            print "counter-->"+str(count)
    return dataList,count
##-------------------------------------------
def dataPerChromFromFile(filename,chomCol,fStartCol,fEndCol,fSourceCol):
    print "reading "+filename
    ##filename the datafile filename
    ##chomCol the column with chrom name
    ##fStartCol the column with feature Start Pos
    ##fEndCol the column with feature End Pos
    dataList=[] #store fileData
    dataPerChromDict={}
    cols=[]
    baseFileName=os.path.basename(filename)
    chomCol=int(chomCol)-1
    fStartCol=int(fStartCol)-1
    fEndCol=int(fEndCol)-1
    fSourceCol=int(fSourceCol)-1
    f = open(filename, 'r')
    goon=True
    count=1
    for line in f:
        cols=line.rstrip().split("\t")
        fChrom=cols[chomCol]
        fStartPos=cols[fStartCol]
        fEndPos=cols[fEndCol]
        fSourceCol=cols[fSourceCol]
#        fLength=int(fEndPos)-int(fStartPos)
        if goon:
            print fChrom
            count+=1;
#            print "counter-->"+str(count)
#    return dataList,count
##--------------------------------------------------------------------
def sortList(aList):
    sList=sorted(aList,key=lambda aList:int(aList[2]) ) ##to 0 dixnei thn prwth column
    return sList
##--------------------------------
def create_chromosome_set(aList,col):
    chromSet=set()
    chrom_list=[]
    for k in aList:
        chromSet.add(k[col-1]) #set to eliminate duplicates
    chrom_list=list(chromSet)
    print chrom_list
    chrom_list=sorted(chrom_list, key=lambda x:Set_Chr_Nr_(x))
    return chrom_list
##--------------------------------
def Set_Chr_Nr_ (Chr):
    """ Sort by chromosome """
    if Chr: 
        New = Chr[3:]
        if New == 'X': New = 23
        elif New == 'Y': New = 24
        elif New == 'M': New = 25
        else: New = int(New)
    else:
        New = 0
    return New
def printListHead(aList,limit):
#    limit=10
    print "print first "+str(limit) 
    cc=0
    for k in  aList:
        print k
        cc+=1
        if limit==cc:
            break
##--------------------------------
def varTest():
    k={}
    k[1]=["a",10,2]
    k[2]=["a",3,4,5]
    k[3]=["b",12,3,3]
    #l=sorted(k.items(),key=lambda a,:a[1][1] )
    print k
    l=sortDict(k)
    print l
    j={}
    j['a']=[k[1],k[2]]
    j['b']=[k[3]]
    print j['a'][1]
    print k.items()
    aList=[['17','27','4'],['16','26','5'],['17','28','3'],['16','26','40'],['16','2','0']]
    bList=sortList(aList)
    print bList
##--------------------------------
def readAllFiles():
    allDataList=[]
    linux=0
    fileList=createFileList(linux)
    fileCount=1
    for fl in fileList:

        dataList=[]
        dataList,count=readData(fl,"1","2","3")
        limit=5
#        printDictHead(dataList,limit)
        fileCount+=1
        allDataList=allDataList+dataList
#    printDictHead(allDataList,limit)
    return allDataList
##--------------------------------
def writeListToFile(outFilename,aList):
    textFile=open(outFilename,"w")
    for k in aList:
        textFile.write(str(k))
        textFile.write("\n")
    textFile.close()
##--------------------------------   

def main():
    allDataList=[]
    chromList=[]
#if __name__ == "__main__":
#    print "start here"
    outFilename="output.txt"
    allDataList=readAllFiles()
    print len(allDataList)
    writeListToFile(outFilename,allDataList)

    allDataListSorted=sortList(allDataList)
    writeListToFile("sorted_"+outFilename,allDataListSorted)
    chromList=create_chromosome_set(allDataListSorted,2)

        
##-------------------------------------------------------

main()

