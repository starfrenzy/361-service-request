# 361-service-request
Microservice for receiving service requests from rental tenants

### What this project does:
This microservice allows a rental tenant to submit a request for maintenance or repair service.

### How to use the microservice:
1. IMPORTANT First Step: Visit the “Building and Installing” section at [this page](https://pypi.org/project/pyzmq/) to install the ZeroMQ Python library.  This is the command:
```
    pip install pyzmq
```
2. Run service_server.py
3. Run service_client.py

#### What to Send:
TBD


#### How to Send:
TBD


#### How to Get the Response:
Read from 'request_list.json'. All new service requests will be posted there. 

Each service request is a separate dictionary in the JSON file.

### UML Diagram

![UML for 361](https://user-images.githubusercontent.com/8403386/181173466-9f362701-cc6b-4d0b-9e16-4c7fe03f7056.jpeg)

###### Jessi Frenzel maintains and contributes to this project.
