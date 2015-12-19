# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "nikos"
__date__ = "$Dec 18, 2015 10:46:24 PM$"

import urllib2
import re
goon=True

urlFirstPage='http://www.skai.gr/player/radiolive/'
request = urllib2.Request(urlFirstPage)
request.add_header('User-Agent', 'FIREFOX LOL')
opener = urllib2.build_opener()
data = opener.open(request).read()
#print data
urls = re.findall(r'href=[\'"]?([^\'" >]+mmid=[\d]+)', data)
urls=["http://www.skai.gr"+s for s in urls]
#print urls

for aUrl in urls:
    print aUrl
    request = urllib2.Request(aUrl)
    request.add_header('User-Agent', 'FIREFOX LOL')
    
    opener = urllib2.build_opener()
    pageHavingMpeUrl = opener.open(request).read()
   print pageHavingMpeUrl
    regEx= re.search("(?P<url>http://download[^\s]+.mp3)", data)
    if regEx is None:goon=False
    if goon:
        fileUrl=group("url")
        print fileUrl
        if 1==2:
            filename=fileUrl.replace("://","_")
            filename=filename.replace("/","-")
            print filename
            request = urllib2.Request(fileUrl)
            request.add_header('User-Agent', 'FIREFOX LOL')
            opener = urllib2.build_opener()
            fileData = opener.open(request).read()
            with open(filename, 'w') as file_:
                file_.write(fileData)




