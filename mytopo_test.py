from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo(Topo):
  "4 hosts, 4 switches"
  def __init__(self):
    Topo.__init__(self)
    h0 = self.addHost('h0')
    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')

    s0 = self.addSwitch('s0')
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')

    self.addLink(h0, s0, delay='0.1ms', max_queue_size=1000)
    self.addLink(h1, s1, delay='0.1ms', max_queue_size=1000)
    self.addLink(h2, s2, delay='0.1ms', max_queue_size=1000)
    self.addLink(h3, s3, delay='0.1ms', max_queue_size=1000)

    self.addLink(s0, s1, delay='1ms', max_queue_size=1000)
    self.addLink(s0, s2, delay='5ms', max_queue_size=1000)
    self.addLink(s0, s3, delay='4ms', max_queue_size=1000)
    self.addLink(s1, s2, delay='2ms', max_queue_size=1000)
    self.addLink(s1, s3, delay='6ms', max_queue_size=1000)
    self.addLink(s2, s3, delay='3ms', max_queue_size=1000)

topos = { 'mytopo': ( lambda: MyTopo() ) }