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
          "Have a great day!\n")

    new_request = {
        "Name": full_name,
        "Phone": phone,
        "Email": email,
        "Issue": issue
        }

    # add dictionary to JSON
    with open("request_list.json", "a") as outfile:
        json.dump(new_request, outfile, indent=1)

    # Send reply back to client
    socket.send_string(f"Service Request: \n {new_request} "
                       f"The new request has been added to request_list.json.")
