#
#   Service Request client in Python
#   Connects REQ socket to tcp://localhost:1999
#   Sends two variables to server as strings, expects the server to add them to a txt
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server 1999...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1999")

weekly_sum = 39.0
payment = 438

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request ...")
    socket.send_string(f"{weekly_sum}, {payment}")

    #  Get the reply.
    message = socket.recv()
    print(f"Received [ {message} ]")
