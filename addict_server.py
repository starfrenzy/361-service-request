#
#   Service Request server in Python
#   Binds REP socket to tcp://*:2000
#   Expects JSON with single dictionary, Adds to JSON of multiple dicts and responds


import json
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2000")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print(f"Received message: {message}")  # receives in bytes

    #  Do some 'work'
    time.sleep(1)

    # add this new dictionary to main JSON
    with open("request_list.json", "a") as outfile:
        json.dump(message, outfile, indent=1)

    # Send reply back to client
    socket.send_string("The new entry has been added to request_list.json.")
