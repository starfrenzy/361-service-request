#
#   Service Request server in Python
#   Binds REP socket to tcp://*:5555
#   Expects "A message from CS361", Sends a tenant's service request back
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1999")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    print("Please enter your information below.")
    full_name = input("Full Name: ")
    phone = input("Phone Number (xxx-xxx-xxxx): ")
    email = input("Email Address: ")
    issue = input("A brief description of your issue: ")
    print("Thank you for submitting your service request.\n"
          "Our office will contact you to arrange service.\n"
          "Have a great day!")

    tenant_issue = {
        "Name" : full_name,
        "Phone" : phone,
        "Email" : email,
        "Issue" : issue
        }

    #  Send reply back to client
    socket.send_string(f"Service Request: {tenant_issue}")