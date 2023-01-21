# Automatic Plate Recognition
The aim of this project is to test new technologies.

# Design
Microservices application to read information from cars plates.
Flask will be used for basic homepage and text extraction from images.

# How to use it
* The only requirement for this project is to have Docker installed. Refers to this page [https://docs.docker.com/get-docker/] if you do not have it. 
* Clone this repo
    ```
    git clone https://github.com/rejamen/plates_recognition.git
    ```
* Go inside the project folder and run this command
    ```
    docker compose up
    ```
* Wait until you see this result in your console
```
INFO:werkzeug: * Restarting with stat
plates_recognition-web-1  | WARNING:werkzeug: * Debugger is active!
plates_recognition-web-1  | INFO:werkzeug: * Debugger PIN: 334-302-545
```
* The App should be running on http://localhot:5001

# Troubleshooting
1. Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5000 -> 0.0.0.0:0: listen tcp 0.0.0.0:5000: bind: address already in use

This means the port is in use by other process in your system. To fix this issue, you can set a different port for this application.
Open the file `docker-compose.yml` and find this section:
```
    web:
        build: .
        ports:
        - "5000:5000"
```
Change it to:
```
    web:
        build: .
        ports:
        - "5001:5000"
```
This will use the port `5001` for our App. Select any free port if `5001` is also in use.