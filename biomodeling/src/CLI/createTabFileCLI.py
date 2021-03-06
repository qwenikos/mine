# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#if __name__ == "__main__":
#    print "Hello World"
from pybel  import *
import datetime
import time
import argparse
import copy
 
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
    smilesDic={}
#    print "Start reading SDF file"+filename;
    ranking_counter=1
    for mol in readfile("sdf", filename):
#        print "-----------------------------------------"
        molData=mol.data
#        print molData
        if  ("code" in molData):
            docDic1[molData['code']]= [ranking_counter]
            ranking_counter+=1
            print ranking_counter
#            enerDic1[molData['code']]=[molData["r_mmod_Potential_Energy-MMFF94s"]]
            enerDic1[molData['code']]=[molData["r_i_docking_score"]]
            smilesDic[molData['code']]=[mol.write("smi").split()[0]]
#            print molData['code']
#            print molData["r_i_docking_score"]
#            print molData["r_mmod_Potential_Energy-MMFF94s"]
#        for k in docDic1:
#            print  docDic1[k]
#    for k in molData:
#        print k+"-->"+molData[k]
    return docDic1,enerDic1,smilesDic
   

#print "end_read SDF file"
#--------------------------------------

def readSdfFileMetadata(filename):
    docDic1={}
    enerDic1={}
#    print "Start reading SDF file"+filename;
    inputfile = readfile("sdf", filename)
    mol = inputfile.next()
    mol = inputfile.next()
#    print mol.write("smi").split()[0]
    
   
#    --------------------------------------

def saveToFile(docDic,smilesDic,numOfFiles,outputFileName):
    text_file = open(outputFileName, "w")
    outLine=""
    outLine+="lines"+"\t"+ str(len(docDic))+"\n"
    outLine+="Files"+"\t"+ str(numOfFiles)+"\n"
    for k in docDic:
        outLine+= str(k)
        outLine+="\t"+str(smilesDic[k])
        for d in docDic[k]:
            outLine+="\t"+str(round(float(d),3))
        outLine+="\n"
    text_file.write(outLine)
    text_file.close()
    return outLine
#    -------------------------------newDocDic-------
def merge(d1, d2):
    merged={}
    ''' Merge two dictionaries. '''
    merged = {}
    merged.update(d1)
    merged.update(d2)
    return merged
##-------------------------------------------------------------------
def createCompoundList(fileList):
    firstLoop=True
    loop=0
    mergedDocDic={}
    mergedEnerDic={}
    for fl in fileList:
        
        print "-->"+fl+"<--"
        loop+=1
        if firstLoop:
            firstLoop=False
            docDic,enerDic,smilesDic=readSdfFile(fl)
            for k in docDic:
                mergedDocDic[k]=docDic[k]
            for k in enerDic:
                mergedEnerDic[k]=enerDic[k]       
        else:

            newDocDic,newEnerDic,smilesDic=readSdfFile(fl)
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
    return docDic
#----------------------------------------------------------------------------------
def createTimeStamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
    return st
##--------------------------------end function definition--------------------------------------------
#------------------------------------MAIN---------------------------------------------------------------
#------------------------------------VARIABLE----------------------------------------------------------
##main program
#print "Starting Here"
numOfFiles=0
st=""
compDic={}
enerDic={}
smilesDic={}
smilesDic={}
fromNetbeans=True 
#-----------------------------------------------------------------------------------------------------------
if fromNetbeans==False:
    parser = argparse.ArgumentParser()
    parser.add_argument("inFile", help="file name for input csv file")
    parser.add_argument("--outFile", help="filename for output bed file")
    args = parser.parse_args()
    inputFilename=args.inFile
    if args.outFile:
        outputFileName= args.outFile
        outToFile=True
else: 
    #############################
    inputPath="/home/nikos/data/"
    filename1="glide-dock_SP_3_23-11_pv.csv"
    filename2=""
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
#    fileList=[sdf_file_test1,sdf_file_test2,sdf_file_test2]
    ##########################

st=createTimeStamp()
outputFileNameRank="output_RANK"+st+".dat"
outputFileNameEnergy="output_ENERGY"+st+".dat"
#readSdfFileMetadata(sdf_file1)
numOfFiles=len(fileList)
compDic=createCompoundList(fileList) #find all  different compound exists in files
energyDic={}
rankDic={}
energyDic=copy.deepcopy(compDic)
rankDic=copy.deepcopy(compDic)
#createTableFromFeatur(compouldsDictionary,dataDictionary)
for fl in fileList:
        newDocDic,newEnerDic,newSmilesDic=readSdfFile(fl)

        
        for k in compDic:
            if k in newDocDic:
                rankDic[k]+=newDocDic[k]
#                print "r->"+str(rankDic[k])
                energyDic[k]+=newEnerDic[k]
#                print "e->"+str(energyDic[k])
                smilesDic[k]=newSmilesDic[k]
            
            else:
                rankDic[k]+=["100000"]
                energyDic[k]+=["0"]


outRankStream=saveToFile(rankDic,smilesDic,numOfFiles,outputFileNameRank)
outEnergyStream=saveToFile(energyDic,smilesDic,numOfFiles,outputFileNameEnergy)
print outRankStream
print"----------"
print outEnergyStream

        
