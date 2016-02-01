#!/usr/bin/python
import cgi
from os import listdir
from os.path import isfile, join
import sys

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
    inputPath="/home/nikos/data/"
    bstr+="<form action='thresholding_step2.py' method='get' >"+"\n" 
    bstr+="<table border=0>"+"\n"
    bstr+="<tr><th></th><th colspan=1>Created At</th><th> [Data from]</th>"

    fileListinDirectory=[]
    fileListinDirectory=createSdfFileList()
    for k in fileListinDirectory:
#        timeStamp=k.rstrip().split("|")[0]
        bstr+="<tr><td><input type='radio' name='filesVersion' value='"+cgi.escape(k).replace("'","")+"'></td><td colspan=2>"+k+"</td></tr>\n"
    bstr+="<tr><td colspan=3 align=center><input type=submit name='submit' value='Go on'></td></tr>"+"\n"
    bstr+="</table>"+"\n"
    bstr+="</form>"+"\n"
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
 ##-------------------------------------------   
def createSdfFileList():
    output=[]
    mypath="./output/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles=[f for f in onlyfiles if f[-3:]=="dat"]
    onlyfiles=[f for f in onlyfiles if f[:8]=="output_R"]
    for fl  in onlyfiles:
        with open(mypath+fl, 'r') as f:
            firstLine = f.readline()
            secondLine = f.readline()
            thirdLine = f.readline()
            onlytimeStamp=fl[11:-4]
            filesInFile=str(thirdLine.rstrip().split("\t"))
            row=onlytimeStamp+"!!"+filesInFile
        output+=[row]
    return output
##-----------------------------------------------
def htmlFooter():
    print "</html>"
#main program
htmlHeader()

htmlBody()
htmlFooter()

