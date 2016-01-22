# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#if __name__ == "__main__":
#    print "Hello World"
from pybel  import *
import datetime
import time
 
def nisnumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False   
#---------------------------------------
def readSdfFile(filename):
    docDic1={}
    enerDic1={}
#    print "Start reading SDF file"+filename;
    for mol in readfile("sdf", filename):
#        print "-----------------------------------------"
        molData=mol.data
        if  "code" in molData:
            docDic1[molData['code']]=[molData["r_i_docking_score"]]
            enerDic1[molData['code']]=[molData["r_mmod_Potential_Energy-MMFF94s"]]
#            print molData['code']
#            print molData["r_i_docking_score"]
#            print molData["r_mmod_Potential_Energy-MMFF94s"]
#    for k in docDic:
#        print  docDic[k]
    return docDic1,enerDic1
#    for k in molData:
#        print k+"-->"+molData[k]

#print "end_read SDF file"

#    --------------------------------------
def saveToFile(docDic,numOfFiles,outputFileName):
    text_file = open(outputFileName, "w")
    outLine=""
    outLine+="lines"+"\t"+ str(len(docDic))+"\n"
    outLine+="Files"+"\t"+ str(numOfFiles)+"\n"
    for k in docDic:
        outLine+= str(k)
        for d in docDic[k]:
            outLine+="\t"+d
        outLine+="\n"
    text_file.write(outLine)
    text_file.close()
    return outLine
#    --------------------------------------
def merge(d1, d2):
    ''' Merge two dictionaries. '''
    merged = {}
    merged.update(d1)
    merged.update(d2)
    return merged
#    --------------------------------------

def readFile(filename):
    global stat_text
#    print filename
    compoundName=''
    columnsDict={}
    tuples=[]
    goon=False
    genes_counter=0
    stranded_counter=0
    genes_tsl1_counter=0
    antistranded_counter=0
    unique_onlycount=0;
    ndict={}
    filtered_dict={}
    ndict_dup={}
    f = open(filename, 'r')
    firstLine=f.readline()
    columns=firstLine.rstrip().split(",")
    i=0;
    for k in columns:
        k=k.strip( '"' )
        columnsDict[k]=i
#        print str(i)+"-->"+k
        i+=1
       
#    print columnsDict["Title"]
#    print columnsDict["Entry ID"]
#    print columnsDict["docking score"]
#    print columnsDict["glide energy"]
    titleNo=columnsDict["Title"]
    entryIdNo=columnsDict["Entry ID"]
    dockingScoreNo=columnsDict["docking score"]
    glideEnergyNo=columnsDict["glide energy"]
    processNum=5
    firstLine=True
    for line in f:
        if firstLine:
             firstLine=False
        else:
            if processNum>0:
                goon=True
                part=line.rstrip().split(",")
                compoundName=part[titleNo]
                compoundRank=part[entryIdNo]
                compoundDockingScore=part[dockingScoreNo]
                if  nisnumeric(compoundDockingScore)==False:
                    goon=False
                compoundEnergy=part[glideEnergyNo]
                if  nisnumeric(compoundEnergy)==False:
                    goon=False
                if goon: 
                    print compoundName,compoundRank,compoundDockingScore,compoundEnergy
                processNum-=1
            else:
                break
##main program
#print "Starting Here"
kcalThreshold=1
rankThreshold=1
numOfFiles=0
st=""
docDic={}
enerDic={}
merged={}
inputPath="/home/nikos/data/"
filename1="glide-dock_SP_3_23-11_pv.csv"
filename2=""
mergedDocDic={}
mergedEnerDic={}
#readFile(inputPath+filename1)


sdf_file1=inputPath+"ALL/1PYS-ALK5.sdf"
sdf_file2=inputPath+"ALL/2WOU-ALK5.sdf"
sdf_file3=inputPath+"ALL/3E93-p38.sdf"
sdf_file4=inputPath+"ALL/3MYO-ALK1.sdf"
sdf_file5=inputPath+"ALL/3Q4U-ALK2.sdf"
sdf_file6=inputPath+"ALL/4BGG-ALK2.sdf"



sdf_file_test1=inputPath+"ALL/test1.sdf"
sdf_file_test2=inputPath+"ALL/test2.sdf"
sdf_file_test3=inputPath+"ALL/test3.sdf"
sdf_file_test4=inputPath+"ALL/test1.sdf"
fileList=[sdf_file1,sdf_file2,sdf_file3,sdf_file4,sdf_file5,sdf_file6]
#fileList=[sdf_file_test1,sdf_file_test2,sdf_file_test3,sdf_file_test4]
#-----------timestamp
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
#----------end timestamp
outputFileName="output_"+st+".dat"
firstLoop=True
loop=0
for fl in fileList:
    numOfFiles=len(fileList)
    print "-->"+fl+"<--"
    loop+=1
    if firstLoop:
        firstLoop=False
        docDic,enerDic=readSdfFile(fl)
        for k in docDic:
            mergedDocDic[k]=docDic[k]
        for k in enerDic:
            mergedEnerDic[k]=enerDic[k]       
    else:

        newDocDic,newEnerDic=readSdfFile(fl)
        mergedDocDic.update(newDocDic)
        mergedEnerDic.update(newEnerDic)
        for k in newDocDic:
            if k in docDic:
                docDic[k]+=newDocDic[k]
            else:
                docDic[k]=newDocDic[k]  
                
        for k in mergedDocDic:
            if k in docDic:
                a=1
            else:
                docDic[k]+=["empty"]
 
for k in docDic:
    docDic[k]=[]

for fl in fileList:
        newDocDic,newEnerDic=readSdfFile(fl)
        for k in docDic:
            if k in newDocDic:
                docDic[k]+=newDocDic[k]
            else:
                docDic[k]+=[""]
                
#
#for k in docDic:
#    print str(k)+"->"+str(docDic[k])

outStream=saveToFile(docDic,numOfFiles,outputFileName)
print outStream

        
