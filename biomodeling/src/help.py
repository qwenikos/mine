#!/usr/bin/python
# -*- coding: utf-8 -*-
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
    ##---------------------------------------------------------
    bstr+="Στον ακόλουθο <a href=''>Σύνδεσμο</a> μπορείτε να μεταφορτώσεται το manual της εφαρμογής σε pdf μορφή"
    bstr+="<body lang='en-US' dir='ltr'>\
        <p lang='el-GR' style='margin-bottom: 0in; line-height: 100%'>FAQ\
</p>\
    <p lang='el-GR' style='margin-bottom: 0in; line-height: 100%'>Ποιοι τύποι αρχείων υποστηρίζονται? \
</p>\
<p lang='el-GR' style='margin-left: 0.49in; margin-bottom: 0in; line-height: 100%'>\
<li>Στην παρούσα έκδοση υποστηρίζονται μόνο SDF αρχεία</p>\
<p lang='el-GR' style='margin-bottom: 0in; line-height: 100%'>Υπάρχει όριο στο μέγεθος των αρχείων που\
 αναφορτώνονται</p>\
<p style='margin-bottom: 0in; line-height: 100%'>	<li>500 ΜΒ</p>\
<p lang='el-GR' style='margin-bottom: 0in; line-height: 100%'>Ποια \
είναι η γραμμογράφηση του αρχείου εξόδου</p>\
<p lang='el-GR' style='margin-bottom: 0in; line-height: 100%'>\
<li>Το αρχείο εξόδου είναι Tab <span lang='en-US'>seperated</span>\
. Οι στήλες του είναι: </p>\
<p style='margin-left: 0.49in; margin-bottom: 0in; line-height: 100%'>\
<li>Compound name</p>\
<p style='margin-left: 0.49in; margin-bottom: 0in; line-height: 100%'>\
<li>Smile bstring</p>\
<p style='margin-left: 0.49in; margin-bottom: 0in; line-height: 100%'>\
<li>[Feature columns] one per file</p>\
<p style='margin-bottom: 0in; line-height: 100%'><br>"
    
    
    
    ##-----------------------------------------------------
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

#main program
htmlHeader()
htmlBody()
htmlFooter()
