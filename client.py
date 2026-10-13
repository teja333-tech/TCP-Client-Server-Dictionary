import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5002))

word = input("Enter a word: ")

client.send(word.encode())

meaning = client.recv(1024).decode()

print("Meaning:", meaning)

client.close()
