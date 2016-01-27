#!/usr/bin/python
import cgi

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
            htmlLine=line.replace("\t","</font></td><td><font Face='Arial' size=1>")
            htmlLine="<tr><td><font Face='Arial' size=1>"+htmlLine+"</font></td></tr>\n"
            outStr+=htmlLine+"\n"
            
            #print line
            
            
        
        
        if i==20000:
            break  
    outStr="<table border=1>"+outStr+"</table>"
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
    energyThres=0
    rankThres=0
    goon=True
    rankThreshold,energyThreshold,refereneceColumn=getFormVar()
    str+="Filtering for<br> "
    if rankThreshold==None:
        str+="Rank Threshold=NONE<br>"
    else:
        str+="Rank Threshold="+rankThreshold+"<br>"
    if energyThreshold==None:
        str+="Energy Threshold=NONE<br>"
    else:      
        str+="Energy Threshold="+energyThreshold+"<br>"
    if refereneceColumn==None:
        str+="referenece Column =NONE<br>"
    else:           
        str+="Column Data="+refereneceColumn+"<br>"
        
    filename= "output_RANK2016-01-27_01_49_34.dat"
#    rankThreshold=2
#    energyThreshold=1
#    refereneceColumn=2#the numbering start at 3
    str+=readDataFromFileToDict(filename,float(rankThreshold),int(refereneceColumn))
    str+= "</section>"+"\n"
    str+="</article>"+"\n"
    str+="<article>"+"\n"
    str+="insert Threshold Values <br>"+"\n"
    str+="</article>"+"\n"
    str+="<footer>"+"\n"
    str+="Nikos Perdikopanis-Biomolecules Modeling-Final Project 2016"+"\n"
    str+="</footer>"+"\n"
    
    str+="</body>"
   
    print str

def htmlFooter():
    print "</html>"
def getFormVar():
    form = cgi.FieldStorage()
    rankTh = str(form.getvalue("rankThreshold"))
    EnergyTh = str(form.getvalue("energyThreshold"))
    BaseFile = str(form.getvalue("base_file"))
    return rankTh,EnergyTh,BaseFile
#main program
htmlHeader()
htmlBody()
htmlFooter()
    
    