#!/usr/bin/python
import cgi
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
    for mol in readfile("sdf", filename):
#        print "-----------------------------------------"
        molData=mol.data
#        print molData
        if  "code" in molData:
            docDic1[molData['code']]=[molData["r_i_docking_score"]]
#            enerDic1[molData['code']]=[molData["r_mmod_Potential_Energy-MMFF94s"]]
            enerDic1[molData['code']]=[molData["r_i_glide_energy"]]
            smilesDic[molData['code']]=[mol.write("smi").split()[0]]
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
#    --------------------------------------
#------------------------------------------------------------------------------------------
def createCompoundList(fileList):
    firstLoop=True
    loop=0
    mergedDocDic={}
    mergedEnerDic={}
    for fl in fileList:
        
#        print "-->"+fl+"<--"
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
def mainCliCall(fileList):
    numOfFiles=0
    st=""
    compDic={}
    enerDic={}
    smilesDic={}
    smilesDic={}
    printStr=""
    inputPath="/home/nikos/data/"
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
                    rankDic[k]+=["100"]
                    energyDic[k]+=["0"]


    outRankStream=saveToFile(rankDic,smilesDic,numOfFiles,outputFileNameRank)
    outEnergyStream=saveToFile(energyDic,smilesDic,numOfFiles,outputFileNameEnergy)
#    print outRankStream
#    print"----------"
#    print outEnergyStream
#------------------------------end from CLI-------------------------------
def readFormParams():
    form = cgi.FieldStorage()
    variable = ""
    value = ""
    r = ""
    for key in form.keys():
            print "n"
            variable = str(key)
            value = str(form.getvalue(variable))
            r += "<p>"+ variable +", "+ value +"</p>\n" 
    fields = "<p>"+ str(r) +"</p>"
    return fields
def readFormFileNames():
    form = cgi.FieldStorage()
    files = form.getvalue("files")
    r=""
    for fl in files:
        r += "<p>"+ "The Files are" +", "+ fl +"</p>\n" 
    filesHtml = "<p>"+ str(r) +"</p>"
    return files,filesHtml

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
    outStr=""
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
            outStr=line+"\n"
            #print line
            
            
        
        
        if i==20000:
            break  
    return outStr


def htmlHeader():
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers
    print  '<html>'+"\n"
    hstr='<head>'+"\n"
    hstr+="<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>"+"\n"
    hstr+="<meta name='robots' content='noindex'>"+"\n"
    hstr+="<META NAME='robots' CONTENT='nofollow'>"+"\n"
    hstr+="<title>bio-molecular_modeling</title>"+"\n"
    hstr+="<link rel='stylesheet' type='text/css' href='normilize.css' />"+"\n"
#    hsrt+="<link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>"+"\n"
    hstr+="</head>"+"\n"
    print hstr

def htmlBody():
    str= "<body>"+"\n"
    str+= "<header><center>"+"\n"
    str+= "ReRank VS results"+"\n"
    str+= "</header></center>"+"\n"
    str+= "<aside>"+"\n"
    str+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"uploadFiles.py\"' name='submit' value='Upload Files' class='menubutton'></td></tr><br>"+"\n"
    str+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"createTableFiles.py\"' name='submit' value='Create-Table- File Files' class='menubutton'></td></tr><br>"+"\n"
    str+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"thresholding.py\"' name='submit' value='Thresholding ' class='menubutton'></td></tr><br>"+"\n"
    str+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"help.py\"' name='submit' value= 'Help' class='menubutton'></td></tr><br>"+"\n"
    str+= "</aside>"+"\n"
    str+= "<article>"+"\n"
    str+= "<section>"+"\n"
#    str+="put data here"+"\n"
    files,filesHtml=readFormFileNames()
    str+=filesHtml
    flList=[]
    for fl in files:
#        print fl
        flList+=[fl]
#    print flList
    mainCliCall(flList)
    str+= "</section>"+"\n"
    str+="</article>"+"\n"
    str+="<article>"+"\n"
#    str+="insert Threshold Values <br>"+"\n"
    str+="</article>"+"\n"
    str+="<footer>"+"\n"
    str+="Nikos Perdikopanis-Biomolecules Modeling-Final Project 2016"+"\n"
    str+="</footer>"+"\n"
    
    str+="</body>"
   
    print str

def htmlFooter():
    print "</html>"

#main program
htmlHeader()
htmlBody()
htmlFooter()
    
    