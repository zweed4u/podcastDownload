import sys, urllib, requests
from clint.textui import progress

counter=0

choice=raw_input('Which podcast do you want to download? (Pick a number)\n\n1.) Rundown\n2.) KFC Radio\n3.) Pardon My Take\n4.) Dave Portnoy Show\n5.) Kat Timpf Show\n6.) Daily Mail\n7.) Mailtime\n8.) Caleb Pressley Show\n\nEnter number: ' )
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
elif choice=='5':
	url='http://www.podcastone.com/the-kat-timpf-show'
	path='KatTimpfShow/'
elif choice=='6':
	url='http://podcastone.com/daily-mail'
	path='DailyMail/'
elif choice=='7':
	url='http://podcastone.com/mailtime'
	path='MailTime/'
elif choice=='8':
	url='http://podcastone.com/the-caleb-pressley-show'
	path='CalebPressleyShow/'

else:
	print 'Please rerun and pick an appropriate number'
	print
	sys.exit()

num=raw_input('How many podcast do you want to download? (11 MAX) ')
try:
	if int(num)<0 or int(num)>12:
		print 'Out of bounds\nPlease rerun and pick a number between 1 and 11'
		sys.exit()
except:
	print 'Choice was NaN\nPlease rerun and try again.\n'
	sys.exit()

print 
session=requests.session()
r=session.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

while counter<int(num):
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
	counter+=1
	print 
print 