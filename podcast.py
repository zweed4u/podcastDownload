import sys, urllib, requests

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      sys.stdout.write("\r" + name + "...%d%%" % percent)
      sys.stdout.flush()

counter=0

choice=raw_input('Which podcast do you want to download? (Pick a number)\n\n1.) Rundown\n2.) KFC Radio\n3.) Pardon My Take\n4.) Dave Portnoy Show\n\nEnter number: ' )
if choice=='1':
	url='http://www.podcastone.com/barstool-rundown'
	path='Rundown/'
elif choice=='2':
	url='http://www.podcastone.com/KFC-Radio'
	path='KFCRadio/'
elif choice=='3':
	url='http://www.podcastone.com/pardon-my-take'
	path='PardonMyTake/'
elif choice=='4':
	url='http://www.podcastone.com/the-dave-portnoy-show'
	path='DavePortnoyShow/'
else:
	print 'Please rerun and pick an appropriate number'
	print
	sys.exit()

num=raw_input('How many podcast do you want to download? (11 MAX) ')
try:
	if int(num)<0 or int(num)>12:
		print 'Out of bounds\nPlease rerun and pick a number between 1 and 11'
except:
	print 'Choice was NaN\nPlease rerun and try again.\n'

print 
session=requests.session()
r=session.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

while counter<int(num):
	link=r.content.split('Download'+str(counter))[0].rsplit('href="',1)[1].replace('\n','').split('" onmouseup=')[0]
	name=r.content.split('Download'+str(counter))[0].rsplit('optLabel="',1)[1].split('" category=')[0].replace('/','-')
	print str(counter+1),'Saving...'
	urllib.urlretrieve(link, path+name+'.mp3', reporthook=dlProgress)
	print
	print name,'saved.'
	counter+=1
	print 
print 