import socket
import bluetooth
import sys
import threading
import time
import csv
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []
sensor_data = []
size=1024

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        #host = "B8:27:EB:97:CB:E1" # .199 The MAC address of a Bluetooth adapter on the server. The server might have mu$
        host = 'B8:27:EB:C8:8E:2E' # .205 The MAC address of a Bluetooth
        port = 2
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connection from multiple clients and saving to a list
# Closing previous connections when server.py file is restarted

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])
            data = conn.recv(size)
    
            if data:
                print(data)
                sensor_data.append(data)
                with open('temphum.csv', 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(['Temperature'] + ['Humidity'])
                    spamwriter.writerow([sensor_data])
            print(sensor_data)	
        except:
            print("Error accepting connections")


#def start_sensing():
#	for c in all_connections:
#		data = all_connections[c].recv(size)
#		if data:
#			print(data)

# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
        
        
# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
            #start_writting()

        queue.task_done()
        
        
        
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()
