'''
This file implements the twsited server that listens for data
on 127.0.0.1:9000 and initiates processes
'''

import subprocess
import logging
from twisted.internet import protocol, reactor


class ProcessControl(protocol.ProcessProtocol):
    '''Class that controls the process'''
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        '''This function is called when process is created'''
        # Increments the process counter
        self.factory.numConnections += 1

    def processEnded(self, reason):
        '''This function is called when process exits'''
        print 'Process Exited'
        # Decrements the process counter
        self.factory.numConnections -= 1


class ProcessRunner(protocol.Protocol):
    '''Class that triggrers the creation of process as it receives message'''
    max_connections = 2     # Maximum number of processes at any instant
    wait_time = 1           # Wait for process completion to start new one

    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        '''Triggered when data is received'''
        print 'Number of connections is: %s' %self.factory.numConnections
        self._start_process()

    def _start_process(self):
        '''Starts a process, waiting if the max number of process reached'''
        
        # If the maximum number of process is reached, it the callLater
        # method to call after some time
        if self.factory.numConnections >= ProcessRunner.max_connections:
            reactor.callLater(ProcessRunner.wait_time, self._start_process)
        else:
            pp = ProcessControl(self.factory)
            command = ['/usr/local/bin/pybot', '-T', 'keyword_driven.txt']
            subprocess = reactor.spawnProcess(pp, command[0], command)


class ProcessFactory(protocol.Factory):
    numConnections = 0

    def buildProtocol(self, addr):
        return ProcessRunner(self)

if __name__ == "__main__":
    reactor.listenTCP(9000, ProcessFactory())
    reactor.run()
