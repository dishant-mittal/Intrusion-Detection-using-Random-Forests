import csv as csv
import numpy as np
from pylab import *
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn import svm
from sklearn.svm import LinearSVC 
#from sklearn.linear_model import SGDClassifier
#csv_file = csv.reader(open('pqr.csv'))
csv_file = csv.reader(open('abc.csv'))
header= csv_file.next()

data = []

for row in csv_file:
	data.append(row)

data = np.array(data)
y=[]

'''
for i in xrange(0,98000):
	if i == 0:
		print data[i]		
	y.append(data[i])
	if i+1 < 98000:
		x=data[i+1]
	
	if x in y:
		n=True
	else:
		n=False
	if n:
		continue
	else:
		if i+1 < 98000:
			print data[i+1]
	
'''
for i in range(0,120000):
	data[i,1] = data[i,1].replace('tcp',"1")
	data[i,1] = data[i,1].replace('udp',"2")
	data[i,1] = data[i,1].replace('icmp',"3")
	data[i,2] = data[i,2].replace('http',"1")
	data[i,2] = data[i,2].replace('smtp',"2")
	data[i,2] = data[i,2].replace('finger',"3")
	data[i,2] = data[i,2].replace('domain_u',"4")
	data[i,2] = data[i,2].replace('auth',"5")
	data[i,2] = data[i,2].replace('telnet',"6")
	data[i,2] = data[i,2].replace('ftp',"7")
	data[i,2] = data[i,2].replace('eco_i',"8")
	data[i,2] = data[i,2].replace('ntp_u',"9")
	data[i,2] = data[i,2].replace('ecr_i',"10")
	data[i,2] = data[i,2].replace('other',"11")
	data[i,2] = data[i,2].replace('private',"12")
	data[i,2] = data[i,2].replace('pop_3',"13")
	data[i,2] = data[i,2].replace('7_data',"14")
	data[i,2] = data[i,2].replace('rje',"15")
	data[i,2] = data[i,2].replace('time',"16")
	data[i,2] = data[i,2].replace('mtp',"17")
	data[i,2] = data[i,2].replace('link',"18")
	data[i,2] = data[i,2].replace('remote_job',"19")
	data[i,2] = data[i,2].replace('gopher',"20")
	data[i,2] = data[i,2].replace('ssh',"21")
	data[i,2] = data[i,2].replace('name',"22")
	data[i,2] = data[i,2].replace('whois',"23")
	data[i,2] = data[i,2].replace('domain',"24")
	data[i,2] = data[i,2].replace('login',"25")
	data[i,2] = data[i,2].replace('imap4',"26")
	data[i,2] = data[i,2].replace('day16',"27")
	data[i,2] = data[i,2].replace('ctf',"28")
	data[i,2] = data[i,2].replace('nntp',"29")
	data[i,2] = data[i,2].replace('shell',"30")
	data[i,2] = data[i,2].replace('IRC',"31")
	data[i,2] = data[i,2].replace('nnsp',"32")
	data[i,2] = data[i,2].replace('1_443',"33")
	data[i,2] = data[i,2].replace('exec',"34")
	data[i,2] = data[i,2].replace('printer',"35")
	data[i,2] = data[i,2].replace('efs',"36")
	data[i,2] = data[i,2].replace('courier',"37")
	data[i,2] = data[i,2].replace('uucp',"38")
	data[i,2] = data[i,2].replace('k25',"39")
	data[i,2] = data[i,2].replace('k30',"40")
	data[i,2] = data[i,2].replace('echo',"41")
	data[i,2] = data[i,2].replace('discard',"42")
	data[i,2] = data[i,2].replace('systat',"43")
	data[i,2] = data[i,2].replace('supdup',"44")
	data[i,2] = data[i,2].replace('iso_tsap',"45")
	data[i,2] = data[i,2].replace('host22s',"46")
	data[i,2] = data[i,2].replace('csnet_ns',"47")
	data[i,2] = data[i,2].replace('pop_2',"48")
	data[i,2] = data[i,2].replace('sunrpc',"49")
	data[i,2] = data[i,2].replace('38_path',"50")
	data[i,2] = data[i,2].replace('netbios_ns',"51")
	data[i,2] = data[i,2].replace('netbios_ssn',"52")
	data[i,2] = data[i,2].replace('netbios_dgm',"53")
	data[i,2] = data[i,2].replace('sql_net',"54")
	data[i,2] = data[i,2].replace('vmnet',"55")
	data[i,2] = data[i,2].replace('bgp',"56")
	data[i,2] = data[i,2].replace('Z39_50',"57")
	data[i,2] = data[i,2].replace('ldap',"58")
	data[i,2] = data[i,2].replace('netstat',"59")
	data[i,2] = data[i,2].replace('urh_i',"60")
	data[i,2] = data[i,2].replace('X11',"61")
	data[i,2] = data[i,2].replace('urp_i',"62")
	data[i,2] = data[i,2].replace('pm_dump',"63")
	data[i,2] = data[i,2].replace('t7_u',"64")
	data[i,2] = data[i,2].replace('tim_i',"65")
	data[i,2] = data[i,2].replace('red_i',"66")
	data[i,3] = data[i,3].replace('SF',"1")
	data[i,3] = data[i,3].replace('S1',"2")
	data[i,3] = data[i,3].replace('REJ',"3")
	data[i,3] = data[i,3].replace('S2',"4")
	data[i,3] = data[i,3].replace('S0',"5")
	data[i,3] = data[i,3].replace('S3',"6")
	data[i,3] = data[i,3].replace('RSTO',"7")
	data[i,3] = data[i,3].replace('RSTR',"8")
	data[i,3] = data[i,3].replace('75',"9")
	data[i,3] = data[i,3].replace('OTH',"10")
	data[i,3] = data[i,3].replace('SH',"11")
	data[i,6] = data[i,6].replace('0',"0")
	data[i,6] = data[i,6].replace('1',"1")
	data[i,11] = data[i,11].replace('0',"0")
	data[i,11] = data[i,11].replace('1',"1")
	data[i,20] = data[i,20].replace('0',"0")
	data[i,20] = data[i,20].replace('1',"1")
	data[i,21] = data[i,21].replace('0',"0")
	data[i,21] = data[i,21].replace('1',"1")
	data[i,41] = data[i,41].replace('normal.',"1")
	data[i,41] = data[i,41].replace('buffer_overflow.',"2")
	data[i,41] = data[i,41].replace('loadmodule.',"3")
	data[i,41] = data[i,41].replace('perl.',"4")
	data[i,41] = data[i,41].replace('neptune.',"5")
	data[i,41] = data[i,41].replace('smurf.',"6")
	data[i,41] = data[i,41].replace('guess_passwd.',"7")
	data[i,41] = data[i,41].replace('pod.',"8")
	data[i,41] = data[i,41].replace('teardrop.',"9")
	data[i,41] = data[i,41].replace('portsweep.',"10")
	data[i,41] = data[i,41].replace('ipsweep.',"11")
	data[i,41] = data[i,41].replace('land.',"12")
	data[i,41] = data[i,41].replace('ftp_write.',"13")
	data[i,41] = data[i,41].replace('back.',"14")
	data[i,41] = data[i,41].replace('imap.',"15")
	data[i,41] = data[i,41].replace('satan.',"16")
	data[i,41] = data[i,41].replace('phf.',"17")
	data[i,41] = data[i,41].replace('nmap.',"18")
	data[i,41] = data[i,41].replace('multihop.',"19")
	data[i,41] = data[i,41].replace('warezmaster.',"20")
	data[i,41] = data[i,41].replace('warezclient.',"21")
	data[i,41] = data[i,41].replace('spy.',"22")
	data[i,41] = data[i,41].replace('rootkit.',"23")

	



xtrain = data[0:68577,0:41].astype(np.float)
ytrain = data[0:68577,41].astype(np.int)
xtest = data[68578:97968,0:41].astype(np.float)
ytest = data[68578:97968,41].astype(np.int)

a=0.0
b=0.0
c=0.0
d=0.0
e=0.0
f=0.0

for index in range(0,68577):
	if ytrain[index] == 10 or ytrain[index] ==11 or ytrain[index] ==18 or ytrain[index] ==16:
		a=a+1
	if ytrain[index] == 5 or ytrain[index] ==8 or ytrain[index] ==14 or ytrain[index] ==12 or ytrain[index] ==6 or ytrain[index] ==9:
		b=b+1
	if ytrain[index] == 2 or ytrain[index] ==3 or ytrain[index] ==4 or ytrain[index] ==23:
		c=c+1
	if ytrain[index] == 13 or ytrain[index] ==15 or ytrain[index] ==7 or ytrain[index] ==19 or ytrain[index] ==17 or ytrain[index] ==22 or ytrain[index] ==20 or ytrain[index] ==21:
		d=d+1
	if ytrain[index] == 1:
		e=e+1
	
print 'number of instances'
print 'probe',a
print 'dos',b
print 'u2r',c
print 'r2l',d
print 'normal',e



print 'percentages:'
print (a/97968.0)*100
print (b/97968.0)*100
print (c/97968.0)*100
print (d/97968.0)*100
print (e/97968.0)*100


