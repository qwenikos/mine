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
    hstr+="<link rel='stylesheet' type='text/css' href='distyle.css' />"+"\n"
    hstr+="</head>"+"\n"
    print hstr

def htmlBody():
    print "<body>"
    inputPath="/home/nikos/data/"
    sdf_file1=inputPath+"ALL/1PYS-ALK5.sdf"
    sdf_file2=inputPath+"ALL/2WOU-ALK5.sdf"
    sdf_file3=inputPath+"ALL/3E93-p38.sdf"
    sdf_file4=inputPath+"ALL/3MYO-ALK1.sdf"
    sdf_file5=inputPath+"ALL/3Q4U-ALK2.sdf"
    sdf_file6=inputPath+"ALL/4BGG-ALK2.sdf"
    str="<form action='2step_web.py' method='get' >"+"\n"
    str+="<table border=1>"
    str+="<tr><td colspan=2 align=right>Rank Threshold     </td><td><input type='text' name='rankThreshold'>"+"</td></tr>\n"
    str+="<tr><td colspan=2 align=right>Energy Threshold</td><td><input type='text' name='energyThreshold'>"+"</td></tr>\n"
    str+="</table>"
    
    str+="<table border=1>"
    str+="<tr><th>Analysis</th><th>Filename</th><th>Base FIle</th>"
    str+="<tr><td><input type='checkbox' name='files[]' value='"+sdf_file1+"'></td><td>"+sdf_file1+" </td><td><input type='radio' name='base_file' value=1>"+"</td></tr>\n"
    str+="<tr><td><input type='checkbox' name='files[]' value='"+sdf_file2+"'></td><td>"+sdf_file2+" </td><td><input type='radio' name='base_file' value=2>"+"</td></tr>\n"
    str+="<tr><td><input type='checkbox' name='files[]' value='"+sdf_file3+"'></td><td>"+sdf_file3+" </td><td><input type='radio' name='base_file' value=3>"+"</td></tr>\n"
    str+= "<tr><td><input type='checkbox' name='files[]' value='"+sdf_file4+"'></td><td>"+sdf_file4+" </td><td><input type='radio' name='base_file' value=4>"+"</td></tr>\n"
    str+="<tr><td><input type='checkbox' name='files[]' value='"+sdf_file5+"'></td><td>"+sdf_file5+" </td><td><input type='radio' name='base_file' value=5>"+"</td></tr>\n"
    str+="<tr><td><input type='checkbox' name='files[]' value='"+sdf_file6+"'></td><td>"+sdf_file6+" </td><td><input type='radio' name='base_file' value=6>"+"</td></tr>\n"
    str+="<tr><td colspan=3 align=center><input type=submit name='submit' value='Go on'></td></tr>"
    str+="</table>"

    str+="</form>"


    print str
    print "</body>"
def htmlFooter():
    print "</html>"

#main program
htmlHeader()
htmlBody()
htmlFooter()