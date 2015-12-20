'''
This file implements the twsited server that listens for data
on Port: 9000 and initiates processes which execute the robot
framework tests
'''

__docformat__ = 'restructuredtext'

import subprocess
import logging
from twisted.internet import protocol, reactor

class TestFileCreator:
    '''
    Class that manipulates files needed for robot framework
    '''
    
    def __init__(self):
        pass
        
    def __create_dir(self, username):
        """
        Return absolute path of directory; create it if it does not exist
        
        Parameter `username`: string, User who has logged in

        Exception: 'CannotCreate' raised if cannot create directory.

        Workflow:
            1. Create a directory if it does not exist.

        """

        pass
    
    
    def __update_test_file(self, scenarioId, action, content):
        """
        Edit a test configuration file based on action

        Parameters:
           
        - `scenarioId`: Scenario for which test file has to be edited
        - `action`: 'create', 'delete' or 'update'
        - `content`: used only during creation; config file contents

        Exception: 'WriteError' raised if cannot update file

        Workflow:
            1. If action='create'; create a file with name scenarioId.
            2. If action='update'; update the file scenarioId with content
            3. If action='delete'; delete the file scenarioId

        """

        pass
    
    
    def __update_database(self, scenarioId, action, name, description):
        """
        Edit database record based on action

        Parameters:
        
        - `scenarioId`: scenario for which test file has to be edited
        - `action`: 'create', 'delete' or 'update'
        - `name`: used only during creation; scenario name
        - `description`: used only during creation; scenario description
        
        Exception: 'WriteError' raised if cannot write database
        
        Workflow:
            1. If action='create'; create a database entry with key as scenarioId.
            2. If action='update'; update the entry corresponding to scenarioId with content
            3. If action='delete'; delete the database entry with key scenarioId

        """

        pass
    
        
    def create_scenario(self, name, description, content):
        """
        Return scenario id; create a robot framework config file
        
        Parameters:
        
        - `name`: name of the scenario
        - `description`: description of the scenario
        - `content`: config file content

        Exception: 'WriteError' raised if cannot create scenario
        
        Workflow:
            1. Create a database entry for the scenario
            2. Create a configuration file for the scenario with content
           
        """
        
        self.__update_database(scenarioId, 'create', name, description)
        
        self.__update_test_file(scenarioId, 'create', content)
        
        pass
        
        
    def update_scenario(self, scenarioId, name, description, content):
        """
        Modify an existing robot framework config file
        
        Parameters: 
        
        - `scenarioId`: scenario to be modified
        - `name`: name of the scenario
        - `description`: description of the scenario
        - `content`: content to be updated with
           
        Exception: 'WriteError' raised if cannot create scenario
        
        Workflow:
            1. Update the scenario in the database with the modified name and description
            2. Update the test file with the updated content
           
        """
        
        self.__update_database(scenarioId, 'update', name, description)
        
        self.__update_test_file(scenarioId, 'update', content)


    def delete_scenario(self, scenarioId):
        """
        Deletes a robot framework config file and updates the db
        
        Parameter: `scenarioId`: scenario to be deleted
        
        Exception: 'WriteError' raised if cannot delete scenario
        
        Workflow:
            1. Delete the scenario with id from the database
            2. Delete the scenario file from the filesystem
           
        """
        
        __update_database(scenarioId, 'delete')
        
        __update_test_file(scenarioId, 'delete')


class MessageSender:
    def __init__(self):
        """
        Creates a message queue and bind to a given ip address
        and port number
           
        Parameters:
        
        - `ip`: ip address to bind to
        - `port`: port number to bind to
        
        Exception: 'CreateError' raised if cannot initialize message queue
        
        Workflow:
            1. Create a PUSH zmq
            2. Bind with the ip address and port number
        
        """
        
        pass
        
        
    def send(self, message):
        """
        Send a message to the socket
        
        Parameter: `message`: message to send
        
        Exception: 'WriteError' raised if cannot send message
        
        Workflow:
            1. Send a message to the socket
        
        """
        
        pass


class MessageReceiver:
    def __init__(self, recv_ip, recv_port, send_ip, send_port):
        """
        Receive message from Message Queue
        
        Parameters:
        
        - `ip`: IP address of the message queue
        - `port`: Port number of the message queue

        Exception:'CreateError' raised if cannot create message queue
        
        Workflow:
            1. Initialize the message queue with type PULL
            2. Create a socket to send message to
            3. Bind to ip address and port number
        
        """
        
        self.__start()


    def __start(self):
        """
        Loop that waits for message to arrive and forward to twisted server
        
        Parameter: None

        Exception: 'ConnectionError' raised if cannot send or receive message

        Workflow:
            1. Wait for messages and send to twisted server
            2. When message arrives forward to sender socket
            3. Close the sender socket
        
        """

    def __read_mq(self, recv_sock):
        """
           Read message from the message queue
           Input: 
              recv_sock - socket to wait for messages
           Output:
              message received
           Exception:
           Workflow:
              1. Read the message queue and return the message
        """
        pass

    def __send_data(self, send_sock, message):
        '''
           Read message from the message queue
           Input: 
              send_sock - socket to send message to
              message - message to send to socket
           Output:
              None
           Exception:
           Workflow:
              1. Send the message to the socket
        '''
        pass


class ProcessRunner(protocol.ProcessProtocol):
    '''
       Class that controls the process
    '''
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        '''
           Called when a connection is made.
           overridden function
        '''
        # Increments the process counter
        self.factory.numConnections += 1

    def processExited(self, reason):
        '''
           Called when the subprocess exits.
           overridden function
        '''
        print 'Process Exited'
        # Decrements the process counter
        self.factory.numConnections -= 1

    def __test_start(self):
        '''
           Tasks to be executed at the beginning of the test
        '''
        pass
        
    def __test_end(self):
        '''
           Tasks to be executed at the end of the test
        '''
        pass

class MessageProcessor(protocol.Protocol):
    '''Class that triggrers the creation of process as it receives message
       and limits the number of processes at any point of time'''
    max_connections = 2     # Maximum number of processes at any instant
    wait_time = 1           # Wait for process completion to start new one

    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        '''
           Called whenever data is received.
           overridden function
        '''
        print 'Number of connections is: %s' % self.factory.numConnections
        self._start_process(params)

    def _start_process(self, params):
        '''
           Starts a process, waiting if the max number of process reached
           Input:
              params: parameters needed for the pybot command
           Output:
              None
           Exception:
           Working:
              1. If the maximum allowed process is reached wait for 
                 it to reduce
              2. Start the process
        '''

        # If the maximum number of process is reached, it the callLater
        # method to pause without consumping cpu cycles
        if self.factory.numConnections >= MessageProcessor.max_connections:
            reactor.callLater(MessageProcessor.wait_time, self._start_process)
        else:
            pp = ProcessRunner(self.factory)
            command = ['/usr/local/bin/pybot', '-T', 'keyword_driven.txt']
            subprocess = reactor.spawnProcess(pp, command[0], command)


class ProcessFactory(protocol.Factory):
    '''This is a factory which produces protocols.'''
    numConnections = 0      # Keeps the count of the connections

    def buildProtocol(self, addr):
        '''
           Create an instance of a subclass of Protocol.
           The returned instance will handle input on an incoming server 
           connection, and an attribute "factory" pointing to the 
           creating factory.
           overridden function
        '''
        return MessageReceiver(self)

if __name__ == "__main__":
    reactor.listenTCP(9000, ProcessFactory())
    reactor.run()
