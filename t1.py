#!/usr/bin/python
import re
import sys
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
    s1=net.addSwitch('s1',protocols='OpenFlow13',listenPort=6673,mac='00:00:00:00:00:01')
    s2=net.addSwitch('s2',protocols='OpenFlow13',listenPort=6674,mac='00:00:00:00:00:02')
    s3=net.addSwitch('s3',protocols='OpenFlow13',listenPort=6675,mac='00:00:00:00:00:03')
    s4=net.addSwitch('s4',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:04')
    s5=net.addSwitch('s5',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:05')
    s6=net.addSwitch('s6',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:06')
    s7=net.addSwitch('s7',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:07')
    s8=net.addSwitch('s8',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:08')
    s9=net.addSwitch('s9',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:09')
    s10=net.addSwitch('s10',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:10')
    s11=net.addSwitch('s11',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:11')
    s12=net.addSwitch('s12',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:12')
    s13=net.addSwitch('s13',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:13')
    s14=net.addSwitch('s14',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:14')
    s15=net.addSwitch('s15',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:15')
    s16=net.addSwitch('s16',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:16')
    s17=net.addSwitch('s17',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:17')
    s18=net.addSwitch('s18',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:18')
    s19=net.addSwitch('s19',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:19')
    s20=net.addSwitch('s20',protocols='OpenFlow13',listenPort=6676,mac='00:00:00:00:00:20')

    h1=net.addHost('h1',mac='00:00:00:00:00:21',ip=hips[1])
    h2=net.addHost('h2',mac='00:00:00:00:00:22',ip=hips[2])
    h3=net.addHost('h3',mac='00:00:00:00:00:23',ip="10.0.0.6/8")
    h4=net.addHost('h4',mac='00:00:00:00:00:24',ip="10.0.0.7/8")
    h5=net.addHost('h5',mac='00:00:00:00:00:25',ip="10.0.0.8/8")
    h6=net.addHost('h6',mac='00:00:00:00:00:26',ip="10.0.0.9/8")
    h7=net.addHost('h7',mac='00:00:00:00:00:27',ip="10.0.0.10/8")
    h8=net.addHost('h8',mac='00:00:00:00:00:28',ip="10.0.0.11/8")
    h9=net.addHost('h9',mac='00:00:00:00:00:29',ip="10.0.0.12/8")
    h10=net.addHost('h10',mac='00:00:00:00:00:30',ip="10.0.0.13/8")

    c = net.addController('c',controller=RemoteController,ip=sys.argv[1],port=6653)

    linkband = dict(bw=30, delay='50ms', loss=0, use_htb=True)
    linkdelay = dict(bw=5, delay='2ms', loss=0, use_htb=True)
    linktohosts= dict(bw=30,delay='2ms',loss=0,use_htb=True)

    net.addLink(s1,h1,**linktohosts)
    net.addLink(s1,h2,**linktohosts)
    net.addLink(s1,h3,**linktohosts)
    net.addLink(s1,s2,**linkband)
    net.addLink(s1,s8,**linkband)
    net.addLink(s2,s3,**linkband)
    net.addLink(s3,s4,**linkband)
    net.addLink(s3,s5,**linkdelay)
    net.addLink(s4,s6,**linkband)
    net.addLink(s5,s6,**linkdelay)
    net.addLink(s6,s7,**linkband)
    net.addLink(s7,s12,**linkband)
    net.addLink(s12,s13,**linkband)
    net.addLink(s12,s14,**linkdelay)
    net.addLink(s13,s15,**linkband)
    net.addLink(s14,s15,**linkdelay)
    net.addLink(s15,h8,**linktohosts)
    net.addLink(s15,h7,**linktohosts)
    net.addLink(s15,h10,**linktohosts)
    net.addLink(s8,s9,**linkband)
    net.addLink(s8,s10,**linkdelay)
    net.addLink(s9,s11,**linkband)
    net.addLink(s10,s11,**linkdelay)
    net.addLink(s11,s16,**linkband)
    net.addLink(s16,s17,**linkband)
    net.addLink(s16,s18,**linkdelay)
    net.addLink(s17,s19,**linkband)
    net.addLink(s18,s19,**linkdelay)
    net.addLink(s19,h4,**linktohosts)
    net.addLink(s19,h5,**linktohosts)

    net.build()
    c.start()
    s20.start([c])
    s19.start([c])
    s18.start([c])
    s17.start([c])
    s16.start([c])
    s15.start([c])
    s14.start([c])
    s13.start([c])
    s12.start([c])
    s11.start([c])
    s10.start([c])
    s9.start([c])
    s8.start([c])
    s7.start([c])
    s6.start([c])
    s5.start([c])
    s4.start([c])
    s3.start([c])
    s2.start([c])
    s1.start([c])

    CLI(net)
    net.stop()

if __name__ == '__main__':

    setLogLevel( 'info' )
    topology()



