#!/usr/bin/python
import sys
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    net = Mininet( controller=RemoteController, link=TCLink,switch=OVSKernelSwitch)
    s1=net.addSwitch('s1',protocols='OpenFlow13',listenPort=6673,mac='00:00:00:00:00:01')
   
    h1=net.addHost('h1',mac='00:00:00:00:00:01',ip="10.0.0.1/8")
    h2=net.addHost('h2',mac='00:00:00:00:00:02',ip="10.0.0.2/8")
   
    c = net.addController('c',controller=RemoteController,ip=sys.argv[1],port=6653)
    linktohosts= dict(bw=30,delay='2ms',loss=0,use_htb=True)

    net.addLink(s1,h1,**linktohosts)
    net.addLink(s1,h2,**linktohosts)
   
    net.build()
    c.start()
    s1.start([c])

    CLI(net)
    net.stop()

if __name__ == '__main__':
        setLogLevel( 'info' )
        topology()
