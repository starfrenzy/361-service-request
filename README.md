# 361-service-request
Microservice for adding dictionaries to a JSON file.

### What this project does:
This microservice takes in a single dictionary and appends it to a JSON file (list) of all dictionaries.

### How to Use the Microservice, What to Send, and How to Send It:
1. IMPORTANT First Step: Visit the “Building and Installing” section at [this page](https://pypi.org/project/pyzmq/) to install the ZeroMQ Python library using Terminal.  This is the command:
```
    pip install pyzmq
```
2. Copy the code in the 'addict_client.py' file in the repository and incorporate it into your program. You need to set it up to send one single dictionary. 
 
_The dictionary stored to a variable on line 16 and used in line 21 in 'addict_client.py' is just an example.  You should delete this and put in the variable name of your new dictionary that you want stored in the JSON file._

Right now the client code is set to send to the server just once. You can update Line 19 to run 'while True' or a certain number of times. If you do that, then indent all following lines. 

3. Make sure to add 'import zmq' to the top of your main program. 
4. Run 'addict_server.py' first before starting your program.


#### How to Get the Response:
Read from 'request_list.json'. Each dictionary you send is a separate dictionary in the JSON file.

### UML Diagram

![UML Send Dictionary](https://user-images.githubusercontent.com/8403386/182536653-81d95bc5-4d6c-4641-96d7-ebb01673242e.png)

###### Jessi Frenzel maintains and contributes to this project.


 
