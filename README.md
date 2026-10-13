# TCP-Client-Server-Dictionary

Project Overview

This project implements a simple dictionary application using Python socket programming. It follows the client-server architecture, where a client sends a word to the server and receives its meaning as a response.

The application uses TCP (Transmission Control Protocol) to establish a connection and exchange data between the client and server.

 Objectives
 
Understand client-server architecture.
Implement TCP communication using Python sockets.
Learn how to send and receive data over a network.
Develop a simple dictionary application using Python.

🛠️ Technologies Used

Python
Socket Programming
TCP (Transmission Control Protocol)

Project Structure

TCP-Client-Server-Dictionary/
├── README.md
├── server.py
└── client.py

⚙️ Working Principle

1. Server

The server creates a TCP socket, binds it to the IP address 127.0.0.1 and port 5002, and listens for incoming connections.

When a client connects, the server receives the requested word and searches for it in a predefined dictionary. If the word exists, the server sends its meaning to the client. Otherwise, it returns "Word not found".

2. Client

The client creates a TCP socket and connects to the server using the same IP address and port.

It accepts a word from the user, sends it to the server, receives the response, displays the meaning, and closes the connection.

Sample Output

Server Output

Server is waiting for connection...
Client connected: ('127.0.0.1', <client_port>)

Note: The client port number varies for each connection.

Client Output

Enter a word: python
Meaning: A high-level programming language.

How to Run the Project

Prerequisite: Python must be installed on your computer.

Step 1: Start the Server

Open a terminal in the project directory and execute:

python server.py

The server will wait for incoming client connections.

Step 2: Start the Client

Open a second terminal in the same directory and execute:

python client.py
Step 3: Enter a Word

Enter a word when prompted. For example:

Enter a word: apple
Meaning: A round fruit that is usually red or green.

The server must be running before you start the client.

 Available Words

The current dictionary contains these predefined words:

apple
computer
python
network
internet

If a word is not present in the dictionary, the server responds with "Word not found".

Limitations

The dictionary contains only five predefined words.
The client and server communicate on the same computer using 127.0.0.1.
The server processes client connections sequentially.
The server must remain running to handle requests.

 Future Enhancements
 
Expand the dictionary with more words and meanings.
Store dictionary entries in a file or database.
Enable communication between different computers.
Support multiple simultaneous clients.
Add a graphical user interface.

Conclusion

This project demonstrates the fundamentals of TCP socket programming and client-server communication using Python. It provides practical experience in establishing connections, exchanging messages, processing client requests, and returning server responses.
