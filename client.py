
import socket
import sys

selection = 0

while selection != 8:

    print("Python DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit\n")

    selection = input("Select: ")
    
    if selection == "1":
        
        data = input("Customer name: ")
        HOST, PORT = "localhost", 9999

        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            print("Server response : " + received + "\n")
        
        sock.close()
        
    elif selection == "2":
        
        name = input("Customer name: ")
        age = input("Customer age: ")
        address = input("Customer address: ")
        number = input("Customer phone number: ")

        data = name + "|" + age + "|" + address + "|" + number
        print(data)
        HOST, PORT = "localhost", 9999


        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print(received)
        sock.close()
        
        #Send customer string to server to add to text file

    elif selection == "3":

        data = input("Customer name to delete: ")
        
        HOST, PORT = "localhost", 9999


        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        
        print(received)
        sock.close()
       

        #Send customer name to server to check if customer exists

    elif selection == "4":

        HOST, PORT = "localhost", 9999

        name = input("Customer name: ")
        new = input("New age: ")
        data = name + "|" + new
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        
        print(received)
        sock.close()

        

    elif selection == "5":
    
        name = input("Customer name: ")
        new = input("New address: ")
        
        HOST, PORT = "localhost", 9999

        data = name + "|" + new
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        
        print(received)
        sock.close()


    elif selection == "6":
        
        name = input("Customer name: ")
        new = input("New phone: ")

        HOST, PORT = "localhost", 9999

        data = name + "|" + new
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print(received)
        sock.close()


    elif selection == "7":
        print("Your selection is " + selection)
        data = "n/a"

        print("** Python DB contents **")

        #send request to server to send list of data
        HOST, PORT = "localhost", 9999

        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(bytes(selection + "*" + data, "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            print(received)
        sock.close()
        #print data

    elif selection == "8":
    
        print("Goodbye!")
        exit()


    else:
        print("Select valid option")
        continue









