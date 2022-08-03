#
#   Service Request client in Python
#   Connects REQ socket to tcp://localhost:1999
#   Sends JSON with single dict, expects server to add to  main JSON of all dicts
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server 2000...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:2000")

weekly_hours = {"hello": "world", "nice": "day"}  # TODO remove - testing only

# Send dictionary as JSON
# Can put 'for request in range(10)', 'while True', etc. here and indent the following
print("Sending dictionary as json ...")
socket.send_json(weekly_hours)

#  Get the reply.
message = socket.recv()
print(f"Received [ {message} ]")
