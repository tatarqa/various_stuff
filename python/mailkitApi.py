import time
import json
import urllib2

start_time = time.time()

req = urllib2.Request('https://api.mailkit.eu/json.fcgi')
req.add_header('Content-Type', 'application/json')
APIlists = {
		'function':'mailkit.mailinglist.list',
		'id': 'xxxx',
		'md5': 'xxxx'
		}
mLists = json.loads(urllib2.urlopen(req, json.dumps(APIlists)).read())
listWalk = iter(list(range(len(mLists))))
pager=10000# max number
statuses=["enabled","disabled","unknown","unsubscribe","permanent"]
fieldSeparator=","
totalRecipients=0
dmInfoOnly=False
iterWalk=True
users=[]
pagedUsers=[]
dmInterests=[]
usersForDb=[]#all user data
dmListId='59377'
fileOutput = open( 'mailkitqq.html', 'w' )
fileOutput.write("<table><tr><th>TITUL</th>")
for status in statuses: fileOutput.write("<th>"+status+"</th>")
fileOutput.write("<th>SUM</th></tr>")
for i in listWalk:
	print str(i)
	if iterWalk is False:
		continue
	if dmInfoOnly is True:
		listId=dmListId
	else:
		listId=mLists[i]['ID_USER_LIST']
		iterWalk=True
	output=[]
	dmIntOutput=[]
	output.append("<tr>")
	listName=mLists[i]['NAME']
	output.append("<td>"+listName.encode('utf-8').strip()+"</td>")
	for x in range(len(statuses)):
		status=""+statuses[x]+""
		req = urllib2.Request('https://api.mailkit.eu/json.fcgi')
		req.add_header('Content-Type', 'application/json')
		try:
			users = json.loads(urllib2.urlopen(req, json.dumps({ "function":"mailkit.mailinglist.getstatus", "id":"xxxx", "md5":"xxxx", "parameters":{ "status":status, "ID_user_list":listId, "ID_email":"0", "limit":pager } })).read())
		except Exception:
			print "something went wrong with this settings:"+status+","+listId+","+pager
			continue
		subscribersSum = len(users)
		totalRecipients=totalRecipients+int(subscribersSum)
		if subscribersSum==pager:
			pagedUsersSum=pager
			lastItem = users[-1]['ID_EMAIL']
			while True:
				req = urllib2.Request('https://api.mailkit.eu/json.fcgi')
				req.add_header('Content-Type', 'application/json')
				pagedUsers = json.loads(urllib2.urlopen(req, json.dumps({ "function":"mailkit.mailinglist.getstatus", "id":"xxxx", "md5":"xxxx", "parameters":{ "status":status, "ID_user_list":listId, "ID_email":lastItem, "limit":pager } })).read())
				for pagedUser in pagedUsers: users.append(pagedUser)
				pagedUsersSum = len(pagedUsers)
				lastItem = pagedUsers[-1]['ID_EMAIL']
				subscribersSum=subscribersSum+pagedUsersSum
				totalRecipients=totalRecipients+pagedUsersSum
				if pagedUsersSum!=pager:
					break
		output.append("<td data-type=\"recipients\" data-state=\""+status+"\">"+str(subscribersSum)+"</td>")
		if listId==dmListId:
			for dmUser in range(len(users)):
				preferedDM=users[dmUser]['CUSTOM_1']
				preferedDM=preferedDM.replace(" ", "")
				if fieldSeparator in preferedDM:
					singleValues = preferedDM.split(fieldSeparator)
					for singleValue in singleValues: dmInterests.append(singleValue)
				else:
					dmInterests.append(preferedDM)
			uniq = set(dmInterests)
			dmIntOutput.append("<tr>")
			for un in uniq:
				dmUsersPerIssueAndState=len(filter(lambda issueType: issueType['CUSTOM_1'] == un, users))
				dmIntOutput.append("<td data-type=\"recipients dmRecipients\" data-state=\""+status+"\" data-interest=\""+un+"\">"+status+"/"+un+":"+str(dmUsersPerIssueAndState)+"</td>")
			dmIntOutput.append("</tr>")
	for row in output: fileOutput.write(row)
	fileOutput.write("<td>"+str(totalRecipients)+"</td></tr>")
	if dmIntOutput:
		for row in dmIntOutput: fileOutput.write(row)
	totalRecipients=0
	if dmInfoOnly is True:
		iterWalk=False
	for user in users: usersForDb.append(user)
fileOutput.write("</table>")
fileOutput.close()

import pickle
with open('mailKomplet.pkl', 'wb') as handle:
	pickle.dump(usersForDb, handle, protocol=pickle.HIGHEST_PROTOCOL)

print "--- %s seconds ---" % (time.time() - start_time)