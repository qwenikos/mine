#!/usr/bin/python
import cgi
import sys

def readDataFromFileToDict(filename,rankThreshold,refereneceColumn):
    f = open(filename, 'r')
    dataDict={}
    outDict={}
    outStr=""
    count=0
    linesNum=f.readline()
    outStr+=str(linesNum)+"<br>\n"
    linesNum=linesNum.rstrip().split("\t")[1]
    columnsNum=f.readline()
    outStr+=str(columnsNum)+"<br>\n"
    columnsNum=columnsNum.rstrip().split("\t")[1]
    FileListStr=f.readline()
    outStr+=str(FileListStr)+"<br>\n"
    
    i=0
    
    for line in f:
        i+=1
        cols=line.rstrip().split("\t")
        compoundName=cols[0]
        smileStr=cols[1]
        dataDict[cols[0]]=[]
        firsrColumn=2
        lastColumn=int(columnsNum)+1
        refColumn=refereneceColumn+1 #efoson xekinan sto 2 
        count=0
        for j in range(firsrColumn,lastColumn+1): #gia kathe compound ypologise th diafora
            if cols[j]=="": #an den yphrxe toy dinw  0 poy einai poly megalo
                cols[j]=0
            if cols[refColumn]=="": #an den yphrxe toy dinw  0 poy einai poly megalo
                cols[refColumn]=0
            difftoRef=float(cols[j])-float(cols[refColumn])
            if difftoRef>rankThreshold:
                count+=1 
        if (count ==int(columnsNum)-1): #an se ola h diafora einai megalyterh apo to threshold
            htmlLine=line.replace("\t","</font></td><td><font Face='Arial' size=1>")
            htmlLine="<tr><td><font Face='Arial' size=1>"+htmlLine+"</font></td></tr>\n"
            htmlLine+="\n"
            outStr+=htmlLine
            outDict[compoundName]=htmlLine
        if i==200000:
            break  
    outStr="<table border=1>"+outStr+"</table>"
    
    return outStr,outDict


def htmlHeader():
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers
    print  '<html>'+"\n"
    hstr='<head>'+"\n"
    hstr+="<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>"+"\n"
    hstr+="<meta name='robots' content='noindex'>"+"\n"
    hstr+="<META NAME='robots' CONTENT='nofollow'>"+"\n"
    hstr+="<title>bio-molecular_modeling</title>"+"\n"
    hstr+="<link rel='stylesheet' type='text/css' href='css/normilize.css' />"+"\n"
#    hsrt+="<link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>"+"\n"
    hstr+="</head>"+"\n"
    print hstr

def htmlBody():
    bstr= "<body>"+"\n"
    bstr+= "<header><center>"+"\n"
    bstr+= "ReRank VS results"+"\n"
    bstr+= "</header></center>"+"\n"
    bstr+= "<aside>"+"\n"
    bstr+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"uploadFiles.py\"' name='submit' value='Upload Files' class='menubutton'></td></tr><br>"+"\n"
    bstr+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"createTableFiles.py\"' name='submit' value='Create-Table- File Files' class='menubutton'></td></tr><br>"+"\n"
    bstr+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"thresholding.py\"' name='submit' value='Thresholding ' class='menubutton'></td></tr><br>"+"\n"
    bstr+="<tr><td colspan=3 align=center><input type=button onclick='location.href=\"help.py\"' name='submit' value= 'Help' class='menubutton'></td></tr><br>"+"\n"
    bstr+= "</aside>"+"\n"
    bstr+= "<article>"+"\n"
    bstr+= "<section>"+"\n"
    energyThres=0
    rankThres=0
    goon=True
    rankThreshold,energyThreshold,refereneceColumn,method,filesVersion=getFormVar()
    energyThreshold==""
    if refereneceColumn==None:
        bstr+="referenece Column =NONE<br>"
    else:           
        bstr+="Column Data="+refereneceColumn+"<br>"     
    filenameEnergy= "output/output_ENERGY"+filesVersion+".dat"
    filenameRank= "output/output_RANK"+filesVersion+".dat"
    sys.stderr.write(refereneceColumn+"\n") 
    sys.stderr.write("Enery File"+filenameEnergy+"\n")
    sys.stderr.write( "Rank File"+filenameRank+"\n")
    if method=="rank":
        bstr+="Filtering with Rank Threshold<br>"
        
        if rankThreshold=="None" or rankThreshold=="" :
            bstr+="Rank Threshold=NONE<br>"
        else:
            
            bstr+="Rank Threshold="+rankThreshold+"<br>"
            outS,outD=readDataFromFileToDict(filenameRank,float(rankThreshold),int(refereneceColumn))
            bstr+=outS
#            print outD
        
    if method=="energy":
        bstr+="Filtering with energy Threshold<br>"
        if energyThreshold=="None" or energyThreshold=="":
            bstr+="Energy Threshold=NONE<br>"
        else:      
            bstr+="Rank Threshold="+rankThreshold+"<br>"
            outS,outD=readDataFromFileToDict(filenameEnergy,float(energyThreshold),int(refereneceColumn))
            bstr+=outS
#            print outD
    if method=="both":
        outDEnergy={}
        outDRank={}
        bstr+="filtering for energy and Ranking thresholds<br>\n"
        if rankThreshold==None:
            bstr+="Rank Threshold=NONE<br>"
        else:
            bstr+="Rank Threshold="+rankThreshold+"<br>"
            outS,outDRank=readDataFromFileToDict(filenameRank,float(rankThreshold),int(refereneceColumn))
        if energyThreshold==None:
            bstr+="Energy Threshold=NONE<br>"
        else:      
            bstr+="Energy Threshold="+energyThreshold+"<br>"
            outS,outDEnergy=readDataFromFileToDict(filenameEnergy,float(energyThreshold),int(refereneceColumn))
        allKeys={}
        for k in outDRank:
            if k in outDEnergy:
                allKeys[k]=1
        for k in outDEnergy:
            if k in outDRank:
                allKeys[k]=1
#        bstr+=str(allKeys)
        
        tempStr=""
        for k in allKeys:
            tempStr+=outDEnergy[k]+"\n"
            tempStr+=outDRank[k]+"\n"
        htmlTable="<table border=1>"+tempStr+"</table>"
        tempStr=tempStr.replace("</font></td><td><font Face='Arial' size=1>","\t")
        tempStr=tempStr.replace("<tr>","")
        tempStr=tempStr.replace("</tr>","")
        tempStr=tempStr.replace("</td>","")
        tempStr=tempStr.replace("<td>","")
        tempStr=tempStr.replace("</font>","")
        tempStr=tempStr.replace("<font Face='Arial' size=1>","")
        tempStr=tempStr.replace("\n\n","\n")
        tempStr=tempStr.replace("\n\n","\n")
        tempStr=tempStr.replace("\n\t","\n")
#        print tempStr
        textFile=open("outputFiltered.txt","w")
        textFile.write(tempStr)
        textFile.close()
        bstr+=htmlTable
        
    bstr+= "</section>"+"\n"
    bstr+="</article>"+"\n"
    bstr+="<article>"+"\n"
#    bstr+="insert Threshold Values <br>"+"\n"
    bstr+="</article>"+"\n"
    bstr+="<footer>"+"\n"
    bstr+="Nikos Perdikopanis-Biomolecules Modeling-Final Project 2016"+"\n"
    bstr+="</footer>"+"\n"
    
    bstr+="</body>"
   
    print bstr

def htmlFooter():
    print "</html>"
def getFormVar():
    form = cgi.FieldStorage()
    rankTh = str(form.getvalue("rankThreshold"))
    EnergyTh = str(form.getvalue("energyThreshold"))
    BaseFile = str(form.getvalue("base_file"))
    sys.stderr.write(BaseFile+"\n") 
    method=str(form.getvalue("method"))
    filesVersion=str(form.getvalue("filesVersion"))
    return rankTh,EnergyTh,BaseFile,method,filesVersion
#main program
htmlHeader()
htmlBody()
htmlFooter()
    
    