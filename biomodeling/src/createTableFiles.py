#!/usr/bin/python
import cgi

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
    inputPath="/home/nikos/data/"
    sdf_file1=inputPath+"ALL/1PYS-ALK5.sdf"
    sdf_file2=inputPath+"ALL/2WOU-ALK5.sdf"
    sdf_file3=inputPath+"ALL/3E93-p38.sdf"
    sdf_file4=inputPath+"ALL/3MYO-ALK1.sdf"
    sdf_file5=inputPath+"ALL/3Q4U-ALK2.sdf"
    sdf_file6=inputPath+"ALL/4BGG-ALK2.sdf"
    str+="<form action='createTableFiles_step2.py' method='get' >"+"\n"
    str+="<table border=0>"+"\n"
    str+="<tr><th>Analysis</th><th>Filename</th>"
    str+="<tr><td><input type='checkbox' name='files' value='"+sdf_file1+"'></td><td>"+sdf_file1+"\n"
    str+="<tr><td><input type='checkbox' name='files' value='"+sdf_file2+"'></td><td>"+sdf_file2+"\n"
    str+="<tr><td><input type='checkbox' name='files' value='"+sdf_file3+"'></td><td>"+sdf_file3+"\n"
    str+= "<tr><td><input type='checkbox' name='files' value='"+sdf_file4+"'></td><td>"+sdf_file4+"\n"
    str+="<tr><td><input type='checkbox' name='files' value='"+sdf_file5+"'></td><td>"+sdf_file5+"\n"
    str+="<tr><td><input type='checkbox' name='files' value='"+sdf_file6+"'></td><td>"+sdf_file6+"\n"
    str+="<tr><td colspan=3 align=center><input type=submit name='submit' value='Create Output FIles'></td></tr>"+"\n"
    str+="</table>"+"\n"
    str+="</form>"+"\n"
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

#main program
htmlHeader()
htmlBody()
htmlFooter()
