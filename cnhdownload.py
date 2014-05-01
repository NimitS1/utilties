import urllib2
import urllib
import re

def get_comic(start):
    response = urllib2.urlopen(start)
    html = response.read()
    m = re.search('<img alt="Cyanide and Happiness, a daily webcomic" src="([^"]+)" border=0>',html)
    if(m != None):
        url = m.group(1)
        file_name = "Comics/"+url.split('/')[-1]
        
        #Checking if the comic actually points to a youtube video. Ignore if that is the case
        if(file_name != 'Comics/play-button.png'):
            urllib.urlretrieve(url,file_name)
            print 'Done:'+file_name
        else:
            print 'Skipping :'+url
    m = re.search('<a rel="next" href="([^"]+)">Next &gt;</a>',html)
    url = ''
    if(m != None):
        url = 'http://explosm.net'+m.group(1)
        print url
    return url

#First comic on explosm
start = 'http://explosm.net/comics/15/'

#Incase you are rerunning, we will run it from the last saved comic
f = open('last_comic','r')
if(f != None):
    start = f.readline()
f.close()

while (start != ''):
    start = get_comic(start)

f = open('last_comic','w')
f.write(start) 
f.close()
print "All comics downloaded"
