'''
This file is used for reading the MQ and send that
data to twisted TCP server at 127.0.0.1:9000
'''

import zmq
import socket
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)

try:
    context = zmq.Context()
    zmq_sock = context.socket(zmq.PULL)
    zmq_sock.bind("tcp://127.0.0.1:5000")
    logging.info('Successfully created message queue')
except:
    logging.error('Could not create message queue')

while True:
    data = zmq_sock.recv()
    logging.info('Received message from zmq')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sock.connect(('127.0.0.1', 9000))
    sock.sendall(data)
    sock.close()
