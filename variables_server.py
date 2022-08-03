#
#   Service Request server in Python
#   Binds REP socket to tcp://*:5555
#   Expects "Connecting ..." message, Sends a tenant's service request back


import json
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1999")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received message: {message}")

    #  Do some 'work'
    time.sleep(1)

    new_entry = {}
    for word in message:
        


    # add dictionary to JSON
    with open("request_list.json", "a") as outfile:
        json.dump(new_entry, outfile, indent=1)

    # Send reply back to client
    socket.send_string("The new entry has been added to request_list.json.")
