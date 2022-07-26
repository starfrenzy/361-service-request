#
#   Service Request client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "A message from CS361" to server, expects a tenant's service request back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1999")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request ...")
    socket.send_string("Please Enter Your Service Request")

    #  Get the reply.
    message = socket.recv()
    print(f"Received [ {message} ]")

    # add to list or JSON of all issues #todo