import os
import sys
import time

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

ADDRESS = os.environ.get('UDP_ADDRESS', '239.0.0.1')  # 239.*.*.*
PORT = int(os.environ.get('UDP_PORT', 1630))  # 1025-65535


class UDPClient(DatagramProtocol):

    def startProtocol(self):
        # Join a specific multicast group
        self.transport.joinGroup(ADDRESS)
        print('Client listening')

    def datagramReceived(self, datagram, address):
        data = datagram.decode('UTF-8')
        print('Client: ' + data)


class UDPServer(DatagramProtocol):

    def startProtocol(self):
        # Set TTL=1 to transmit over the local network only
        self.transport.setTTL(1)
        self.transport.joinGroup(ADDRESS)

        n = 0
        while 1:
            n += 1/60
            number = '{0:.2f}'.format(n)
            message = bytes(number, 'UTF-8')
            self.transport.write(message, (ADDRESS, PORT))

            print('Server: ' + number)
            time.sleep(1/60)


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == '--client':
        # Use listenMultiple=True to run client and server on the same machine
        reactor.listenMulticast(PORT, UDPClient(), listenMultiple=True)
    else:
        reactor.listenMulticast(PORT, UDPServer(), listenMultiple=True)

    reactor.run()
