#
#   Service Request server in Python
#   Binds REP socket to tcp://*:5555
#   Expects "A message from CS361", Sends a tenant's service request back
#
import json
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1999")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")
    time.sleep(1)

    #  Do some 'work'
    #  add new dictionary to a JSON of all issues
    with open("request_list.json", "a") as outfile:
        json.dump(dictionary, outfile)

    #  Send reply back to client
    socket.send_string(f"Service Request added to {outfile}")