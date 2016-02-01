#!/usr/bin/python
import cgi
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
    filesVersion,fileList=getFormVar()
#    fileList=["file1","file","file3"]
    bstr+="<form action='thresholding_step3.py' method='get' >"+"\n"
    bstr+="<table border=0>"+"\n"
#    bstr+="-->"+str(filesVersion)+"<--"
    
    bstr+="<tr><td colspan=2 align=right>Rank Threshold     </td><td colspan=4><input type='text' name='rankThreshold'>"+"</td></tr>"+"\n"
    bstr+="<tr><td colspan=2 align=right>Energy Threshold</td><td colspan=4><input type='text' name='energyThreshold'>"+"</td></tr>"+"\n"
    bstr+="<td>"+"Rank Filter"+" </td><td><input type='hidden' name='filesVersion' value='"+filesVersion+"'>"+"</td>"+"\n"
    bstr+="<td>"+"Rank Filter"+" </td><td><input type='radio' name='method' value=rank checked=checked>"+"</td>"+"\n"
    bstr+="<td>"+"Energy Filter"+" </td><td><input type='radio' name='method' value=energy>"+"</td>"+"\n"
    bstr+="<td>"+"Both"+" </td><td><input type='radio' name='method' value=both>"+"</td></tr>"+"\n"
    bstr+="</table>"+"\n"
    
    bstr+="<table border=0>"+"\n"
    bstr+="<tr><th colspan=6>Referece File</th><th></th>"
    i=1
    for fl in fileList:
        if i==1:
            bstr+="<tr><td colspan=6>"+fl+" </td><td align=center><input type='radio' name='base_file' value="+str(i)+" checked=checked>"+"</td></tr>"+"\n"
        else:
            bstr+="<tr><td colspan=6>"+fl+" </td><td align=center><input type='radio' name='base_file' value="+str(i)+"></td></tr>"+"\n"
        i+=1
        
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
##--------------------------------------------------------
def getFormVar():
    form = cgi.FieldStorage()
    filesVersion = str(form.getvalue("filesVersion"))
    
#    sys.stderr.write(">filesVersion>"+filesVersion+"<<\n")
    timeStamp=filesVersion.rstrip().split("!!")[0]
    sys.stderr.write(">timeStamp>"+timeStamp+"<<\n")
    fileList=filesVersion.rstrip().split("!!")[1]
    sys.stderr.write(">fileList>"+fileList+"<<\n")
    fileList=fileList.replace("[","")
    fileList=fileList.replace("]","")
    fileList=fileList.rstrip().split(",")
    return timeStamp,fileList
##----------------------------------------------------------
def htmlFooter():
    print "</html>"
#main program
htmlHeader()

htmlBody()
htmlFooter()
