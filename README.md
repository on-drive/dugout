# dugout

A chat tool with a simple command-line interface which supports multiple chat rooms.

## How does server works

- Create socket
- Communicate the socket address
- Keep waiting for an incoming connection request/s
- Connect to client
- Receive the message
- Decode the destination user and select the socket
- Send a message to the intended client
- Keep repeating step 5 & 6 as per users wish
- Exit i.e. end the communication by terminating the connection

## How does client works

- Create a unique client socket per instance/user
- Connect to the server with given socket address (IP and port)
- Send and receive messages
- Repeat step 3 as per configuration
- Close the connection
