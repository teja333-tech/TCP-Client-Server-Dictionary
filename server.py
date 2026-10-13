import socket

dictionary = {
    "apple": "A round fruit that is usually red or green.",
    "computer": "An electronic device used to process data.",
    "python": "A high-level programming language.",
    "network": "A group of connected computers.",
    "internet": "A worldwide network of computers."
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5002))
server.listen(5)

print("Server is waiting for connection...")

while True:
    client, address = server.accept()
    print("Client connected:", address)

    word = client.recv(1024).decode().lower()

    if word in dictionary:
        meaning = dictionary[word]
    else:
        meaning = "Word not found"

    client.send(meaning.encode())
    client.close()
