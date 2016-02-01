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
    sdf_file1=inputPath+"ALL/1PYS-ALK5.sdf"
    sdf_file2=inputPath+"ALL/2WOU-ALK5.sdf"
    sdf_file3=inputPath+"ALL/3E93-p38.sdf"
    sdf_file4=inputPath+"ALL/3MYO-ALK1.sdf"
    sdf_file5=inputPath+"ALL/3Q4U-ALK2.sdf"
    sdf_file6=inputPath+"ALL/4BGG-ALK2.sdf"
    bstr+="<form action='createTableFiles_step2.py' method='get' >"+"\n"
    bstr+="<table border=0>"+"\n"
    bstr+="<tr><th>Analysis</th><th>Filename</th>"
    
#    bstr+="<tr><td><input type='checkbox' name='files' value='"+sdf_file1+"'></td><td>"+sdf_file1+"</td></tr>\n"
#    bstr+="<tr><td><input type='checkbox' name='files' value='"+sdf_file2+"'></td><td>"+sdf_file2+"</td></tr>\n"
#    bstr+="<tr><td><input type='checkbox' name='files' value='"+sdf_file3+"'></td><td>"+sdf_file3+"</td></tr>\n"
#    bstr+= "<tr><td><input type='checkbox' name='files' value='"+sdf_file4+"'></td><td>"+sdf_file4+"</td></tr>\n"
#    bstr+="<tr><td><input type='checkbox' name='files' value='"+sdf_file5+"'></td><td>"+sdf_file5+"</td></tr>\n"
#    bstr+="<tr><td><input type='checkbox' name='files' value='"+sdf_file6+"'></td><td>"+sdf_file6+"</td></tr>\n"
#    bstr+="<tr><td>-----</td><td>----</td></tr>\n"
    fileListinDirectory=[]
    fileListinDirectory=createSdfFileList()
    for k in fileListinDirectory:
       bstr+="<tr><td><input type='checkbox' name='files' value='"+k+"'></td><td>"+k+"\n"
       
    bstr+="<tr><td colspan=3 align=center><input type=submit name='submit' value='Create Output FIles'></td></tr>"+"</td></tr>\n"
    bstr+="</table>"+"\n"
    bstr+="</form>"+"\n"
#    bstr+=str(createSdfFileList())
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

def createSdfFileList():
    mypath="./inputSDF/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles=[f for f in onlyfiles if f[-3:]=="sdf"]
#    sys.stderr.write(str(onlyfiles)+".\n")
    return onlyfiles
    
def htmlFooter():
    print "</html>"

#main program
htmlHeader()
htmlBody()
htmlFooter()
