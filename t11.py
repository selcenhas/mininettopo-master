#!/usr/bin/python
import re
import sys
import itertools
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

	
def topology():

    hostcount=500
    swcount=30

    with open('nodes.txt') as f:
	lines = f.readlines()


    #lines 1-30 arasi switchler, 31-531 arasi hostlar
    #print lines[30]

    hips={}
    i=1
    while i<hostcount+1:
	tline=re.split(r'\t+', lines[i+30])
	hips[i]=tline[1]
	i=i+1
		
    net = Mininet( controller=RemoteController, link=TCLink,switch=OVSKernelSwitch)

#switchleri ekleme
    allmacs={}
    i=0
    for x, y in itertools.product(xrange(50), xrange(50)):
        allmacs[i]="00:00:00:00:{:02x}:{:02x}".format(x,y)
        i=i+1
    
    SwArr={}
    swname=""
    port=6673
    i=1
    while i<swcount+1:
	swname="s"+str(i)
	SwArr[i]=net.addSwitch(swname,protocols='OpenFlow13',listenPort=port+i,mac=allmacs[i])
	i=i+1 
   
#hostlari ekleme
    HostArr={}
    hostname=""
    i=1
    while i<hostcount+1:
	hostname="h"+str(i)
	HostArr[i]=net.addHost(hostname,ip=hips[i])
	i=i+1

#controller ekleme
    c = net.addController('c',controller=RemoteController,ip=sys.argv[1],port=6653)
	
#link types
    linkband = dict(bw=30, delay='50ms', loss=0, use_htb=True)
    linkdelay = dict(bw=5, delay='2ms', loss=0, use_htb=True)
    linktohosts= dict(bw=30,delay='2ms',loss=0,use_htb=True)

#linkleri ekleme(host-sw)
    numofsubnet=5
    hostPersubnet=hostcount/numofsubnet #bizimki 100
    numofswInSubnet=5
    hostPersw=hostPersubnet/numofswInSubnet #bizimki 20

    i=1
    swix=1#sw index
    while i<hostcount+1:
	#print "swix "+str(swix)+" host"+str(i)
	net.addLink(SwArr[swix],HostArr[i],**linktohosts)
	if (i%20)==0:
		swix=swix+1	
	if (i%100)==0:
		swix=swix+1
	i=i+1

#linkleri ekleme(sw-sw)	
    net.addLink(SwArr[1],SwArr[2],**linkband)
    i=0
    while i<numofsubnet:
	net.addLink(SwArr[1+6*i],SwArr[3+6*i],**linkband)
	net.addLink(SwArr[1+6*i],SwArr[4+6*i],**linkband)
	net.addLink(SwArr[2+6*i],SwArr[4+6*i],**linkband)
	net.addLink(SwArr[2+6*i],SwArr[5+6*i],**linkband)
	net.addLink(SwArr[3+6*i],SwArr[5+6*i],**linkband)
	net.addLink(SwArr[4+6*i],SwArr[6+6*i],**linkband)
	net.addLink(SwArr[5+6*i],SwArr[6+6*i],**linkband)
	i=i+1
	
	
#linkleri ekleme(gsw-gsw)
    net.addLink(SwArr[6],SwArr[12],**linkband)
    net.addLink(SwArr[6],SwArr[18],**linkband)
    net.addLink(SwArr[6],SwArr[24],**linkband)
    net.addLink(SwArr[6],SwArr[30],**linkband)

    net.addLink(SwArr[12],SwArr[18],**linkband)
    net.addLink(SwArr[12],SwArr[24],**linkband)
    net.addLink(SwArr[12],SwArr[30],**linkband)
	
    net.addLink(SwArr[18],SwArr[24],**linkband)
    net.addLink(SwArr[18],SwArr[30],**linkband)
	
    net.addLink(SwArr[24],SwArr[30],**linkband)


#switchleri baslatma
    net.build()
    c.start()
	
    i=1
    while i<swcount+1:
        SwArr[i].start([c])
	i=i+1 	
		
    CLI(net)
    net.stop()

	
if __name__ == '__main__':

    setLogLevel( 'info' )
    topology()



