#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
import os
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
    hstr+="<link rel='stylesheet' type='text/css' href='normilize.css' />"+"\n"
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
##inser data here
    UPLOAD_DIR="/home/nikos/biothesis/github/mine/biomodeling/src"
#    bstr+= printFileData("userfile1")
    formFieldList=["userfile1","userfile2","userfile3","userfile4","userfile5","userfile6"]
    bstr+=save_uploaded_file (formFieldList, UPLOAD_DIR)

#    bstr+=save_uploaded_file ("userfile1", UPLOAD_DIR)
#    bstr+=save_uploaded_file ("userfile2", UPLOAD_DIR)
#    bstr+=save_uploaded_file ("userfile3", UPLOAD_DIR)
#    bstr+= save_uploaded_file ("userfile4", UPLOAD_DIR)
#    bstr+=save_uploaded_file ("userfile5", UPLOAD_DIR)
#    bstr+=save_uploaded_file ("userfile6", UPLOAD_DIR)

##end insert data hera
    bstr+= "</section>"+"\n"
    bstr+="</article>"+"\n"
    bstr+="<article>"+"\n"
    bstr+="</article>"+"\n"
    bstr+="<footer>"+"\n"
    bstr+="Nikos Perdikopanis-Biomolecules Modeling-Final Project 2016"+"\n"
    bstr+="</footer>"+"\n"
    
    bstr+="</body>"
   


    print bstr
##------------------------------------------------------------------
def htmlFooter():
    print "</html>"
##------------------------------------------------------------------
def getFormVar(formFiledName):
    form = cgi.FieldStorage()
    userfiles = str(form.getvalue(formFiledName))
    return userfiles
##------------------------------------------------------------------
def printFileData(fieldName):
    form = cgi.FieldStorage()
    # A nested FieldStorage instance holds the file
    fileitem = form['userfile1']
    output= "----"
    output+= fieldName+"-->"+str( fileitem.filename)
    output+="file-->"+str( fileitem.file)
    output+="----"
    return output
    
def save_uploaded_file (form_field_list, upload_dir):
    output=""
    form = cgi.FieldStorage()
    for form_field  in form_field_list:
        goon=True
        
        if not form.has_key(form_field): 
            return "nokey<br>"
            goon=False
        fileitem = form[form_field]
        if not fileitem.file: 
            return "noItem<br>"
            goon=False
        if fileitem.filename=="":
            fileitem.filename
            output+="blank<br>"
            goon=False
    #    fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
        
        if goon==True:
            fout=file(fileitem.filename,'wb')
            output+="loop<br>"
            while 1:
                chunk = fileitem.file.read(100000000)
#                output+=chunk
                if not chunk: break
                fout.write (chunk)
            fout.close()
            output+="finito "+fileitem.filename+"<br>"
    return output

#main program
htmlHeader()
htmlBody()
htmlFooter()
