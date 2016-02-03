# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
def readData(filename,chomCol,fStartCol,fEndCol):
    ##filename the datafile filename
    ##chomCol the column with chrom name
    ##fStartCol the column with feature Start Pos
    ##fEndCol the column with feature End Pos
    dataDict={} #store fileData
    cols=[]
    chomCol=int(chomCol)-1
    fStartCol=int(fStartCol)-1
    fEndCol=int(fEndCol)-1
    f = open(filename, 'r')
    goon=True
    count=0
    for line in f:
        cols=line.rstrip().split("\t")
        fChrom=cols[chomCol]
        fStartPos=cols[fStartCol]
        fEndPos=cols[fEndCol]
        fLength=int(fEndPos)-int(fStartPos)
        if goon:
            dataDict[count]=[fChrom,fStartPos,fEndPos]
            count+=1;
#            print "counter-->"+str(count)
    return dataDict,count
##-------------------------------------------
def sortDict(aDict):
    l={}
    l=sorted(aDict.items(),key=lambda a:a[1][1] ) ##to 0 dixnei thn prwth column
    bDict={}
    for k in l:
        bDict[k[0]]=k[1]
    return bDict
##--------------------------------
def create_chromosome_set(aDict):
    chromSet=set()
    chrom_list=[]
    for k in aDict:
#        print aDict[k][0]
        chromSet.add(aDict[k][0]) #set to eliminate duplicates
    chrom_list=list(chromSet)
#    print chrom_list
    return chrom_list
def main():
#if __name__ == "__main__":
#    print "start here"
    filename1="/home/nikos/biothesis/data/Human/ChIPseq/Pol2/ESC/GSM822300/macs/Pol2_peaks.bed"
    filename2="/home/nikos/biothesis/data/Human/ChIPseq/H3K4me3/ESC/GSM605315/sicer/w200_g400/accepted_hits_noDupl-W200-G400.scoreisland"
    dataDict1,count1=readData(filename1,"1","2","3")
    chromList1=create_chromosome_set(dataDict1)
    print count1
    print dataDict1[0]
    print str(chromList1)  
    dataDict2Sorted=sortDict(dataDict1)
    
    dataDict2,count2=readData(filename2,"1","2","3")
    chromList2=create_chromosome_set(dataDict2)
    print count2
    print dataDict2[0]
    print str(chromList2)
    print dataDict2Sorted
    cc=0
    for k in  dataDict2Sorted:
        print dataDict2Sorted[k]
        cc+=1
        if cc==10:
            break
    
    
k={}
k[1]=["a",10,2]
k[2]=["a",3,4,5]
k[3]=["b",12,3,3]
#l=sorted(k.items(),key=lambda a,:a[1][1] )
print k
l=sortDict(k)
print l
#print k.items()
#main()
