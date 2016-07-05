import sys, urllib, requests

def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	sys.stdout.write("\r" + date+' // '+name + "...%d%%" % percent)
	sys.stdout.flush()

counter=0
pathCount=0
urlPick=['barstool-rundown','KFC-Radio','pardon-my-take','the-dave-portnoy-show','the-kat-timpf-show','daily-mail','mailtime','the-caleb-pressley-show']
pathPick=['Rundown/','KFCRadio/','PardonMyTake/','DavePortnoyShow/','KatTimpfShow/','DailyMail/','MailTime/','CalebPressleyShow/']

print 
session=requests.session()
for url in urlPick:
	r=session.get('http://podcastone.com/'+url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	path=pathPick[pathCount]
	print 'Downloading',path.split('/')[0]
	while counter<3:
		date=r.content.split('float:right; width:70px; text-align:right;">')[counter+1].split('&nbsp;')[0].replace('/','-')
		link=r.content.split('Download'+str(counter))[0].rsplit('href="',1)[1].replace('\n','').split('" onmouseup=')[0]
		name=r.content.split('Download'+str(counter))[0].rsplit('optLabel="',1)[1].split('" category=')[0].replace('/','-')
		print str(counter+1),'Saving...'
		urllib.urlretrieve(link, path+date+' :: '+name+'.mp3', reporthook=dlProgress)
		print
		print date+' // '+name,'saved.'
		counter+=1
		print 
	counter=0
	pathCount+=1
	print 