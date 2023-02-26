import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(2048).decode()
        input = str(self.data).split('*')
        

        selection = input[0]
        data = input[1]
        
        print("{} wrote:".format(self.client_address[0]))
        print(selection + " " + data)
        
        if selection == "1":
            valid = False

            fin = open("data.txt", "r")

            for line in fin:
                if data in line:
                    self.request.send(bytes(line, "utf-8"))
                    valid = True

            if valid == False:
                self.request.send(bytes(data + " not found in database", "utf-8"))

            fin.close()

        if selection == "2":
            valid = True

            data = data.split('|')

            fin = open("data.txt", "r+")

            name = data[0]
            
            for line in fin:
                
                if name in line:
                    
                    valid = False
                    self.request.send(bytes("Customer already exists", "utf-8"))
                    break
                
                    

            if valid == True:
                
                fin.write('\n')
                fin.write(data[0] + "|" + data[1] + "|" + data[2] + "|" + data[3])
                self.request.send(bytes("Customer successfully added to database", "utf-8"))

            fin.close()
        
        if selection == "3":
            valid = False
            counter = 0
            fin = open("data.txt", "r")

            words = fin.readlines()
            fin.seek(0,0)
            for line in fin:
                
                if data in line:
                    valid = True
                    words[counter] = ""
                
                counter = counter + 1
            
            fin.close()

            fout = open("data.txt", "w")
            fout.writelines(words)

            fout.close()

            if valid == True:
                self.request.send(bytes("Customer successfully deleted", "utf-8"))
            else:
                self.request.send(bytes("Customer does not exist", "utf-8"))
        
        if selection == "4":
            valid = False
            counter = 0
            glue = "|"
            
            fin = open("data.txt", "r")

            words = fin.readlines()
            fin.seek(0,0)

            data = data.split("|")
           
            for line in fin:
                
                if data[0] in line:
                    
                    valid = True
                    
                    words[counter] = words[counter].split("|")
                    
                    words[counter][1] = data[1]
                    words[counter] = glue.join(words[counter])
                    
                    

                counter = counter + 1
            
            fin.close()

            fout = open("data.txt", "w")
            fout.writelines(words)

            fout.close()

            if valid == True:
                self.request.send(bytes("Age successfully changed", "utf-8"))
            else:
                self.request.send(bytes("Customer does not exist", "utf-8"))

        if selection == "5":
            valid = False
            counter = 0
            glue = "|"
            
            fin = open("data.txt", "r")

            words = fin.readlines()
            fin.seek(0,0)

            data = data.split("|")
           
            for line in fin:
                
                if data[0] in line:
                    
                    valid = True
                    
                    words[counter] = words[counter].split("|")
                    
                    words[counter][2] = data[1]
                    words[counter] = glue.join(words[counter])
                    
                    

                counter = counter + 1
            
            fin.close()

            fout = open("data.txt", "w")
            fout.writelines(words)

            fout.close()

            if valid == True:
                self.request.send(bytes("Address successfully changed", "utf-8"))
            else:
                self.request.send(bytes("Customer does not exist", "utf-8"))
        
        if selection == "6":
            valid = False
            counter = 0
            glue = "|"
            
            fin = open("data.txt", "r")

            words = fin.readlines()
            fin.seek(0,0)

            data = data.split("|")
           
            for line in fin:
                
                if data[0] in line:
                    
                    valid = True
                    
                    words[counter] = words[counter].split("|")
                    
                    words[counter][3] = data[1]
                    words[counter] = glue.join(words[counter])
                    
                    

                counter = counter + 1
            
            fin.close()

            fout = open("data.txt", "w")
            fout.writelines(words)

            fout.close()

            if valid == True:
                self.request.send(bytes("Number successfully changed", "utf-8"))
            else:
                self.request.send(bytes("Customer does not exist", "utf-8"))
        
        if selection == "7":
            lines = ''
            fin = open("data.txt", "r")
            for line in fin:
                lines = lines + line.replace('\\n', '\n')

            self.request.send(bytes(lines, "utf-8"))

            fin.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()