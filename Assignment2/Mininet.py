#!/usr/bin/python


from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.cli import CLI

import sys

if len(sys.argv) < 3:
	print "Write No of Hosts and Switches"
	sys.exit(1)

NoOfHosts=int(sys.argv[1])
NoOfSwitches=int(sys.argv[2])

def emptyNetwork():

    "Creatng Void network ...."

    net = Mininet( controller=Controller , link=TCLink)
    info( 'Adding controller ...\n' )
    net.addController( 'c0' )
    info( 'Adding hosts ...\n' )
    switches=[]
    ipEven='11.0.0.'
    IpOdd='11.0.1.'

    even=1
    odd=1
    hosts=[]

    for i in range(1,NoOfHosts*NoOfSwitches+1):
    
        if i%2==0:
            hosts.append(net.addHost('h'+str(i), ip=ipEven+str(even)+'/24'))
            even=even + 1
        else:
            hosts.append(net.addHost('h'+str(i), ip=IpOdd+str(odd)+'/24'))
            odd= odd + 1


        print "h"+str(i) + " Added"

    info( 'Adding switch ...\n' )

    for i in range(1,NoOfSwitches+1):
        switches.append(net.addSwitch('s'+str(i)))
        print "s"+str(i) + " Added"

    info( 'Adding links ...\n' )
    
    bandwidth=0
    for i in range(0,NoOfSwitches-1):
        net.addLink(switches[i],switches[i+1],bw=2)
        print "s"+str(i)+"<--->s"+str(i+1)

    for i in range(0,NoOfSwitches):
        for j in range(0,NoOfHosts):
            net.addLink( hosts[NoOfHosts*i+j], switches[i] , bw=bandwidth+1)
            bandwidth=(bandwidth+1)%2
            print "h"+str(NoOfHosts*i+j+1)+"<--->s"+str(i)
            
    info( 'Starting network ....\n')
    net.start()
    CLI( net )
    info( 'Stopping network ....' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )

    emptyNetwork()
