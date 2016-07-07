import sys, urllib, requests
from clint.textui import progress

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
	print
	while counter<3:
		date=r.content.split('float:right; width:70px; text-align:right;">')[counter+1].split('&nbsp;')[0].replace('/','-')
		link=r.content.split('Download'+str(counter))[0].rsplit('href="',1)[1].replace('\n','').split('" onmouseup=')[0]
		name=r.content.split('Download'+str(counter))[0].rsplit('optLabel="',1)[1].split('" category=')[0].replace('/','-')
		print str(counter+1),'Saving...'
		res = session.get(link, stream=True)
		print date+' // '+name 
		with open(path+date+' :: '+name+'.mp3', 'wb') as f:
		    total_length = int(res.headers.get('content-length'))
		    for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
		        if chunk:
		            f.write(chunk)
		            f.flush()
		print 'Saved.'
		print
		counter+=1 
	counter=0
	pathCount+=1
	print 