from multiprocessing import Process
import socket

def controll_to_rover(client_socket,client_socket_rover):
    while True:
        msg = client_socket.recv(8192)
        client_socket_rover.send(msg)

def rover_to_controll(client_socket,client_socket_rover):
    while True:
        msg = client_socket_rover.recv(8192)
        client_socket.send(msg)

def run():
    server_socket_rover = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = "192.168.1.164"
    port = 6969
    port_rover = 6970
    socket_address_rover = (host_ip, port_rover)
    socket_address = (host_ip, port)
    server_socket_rover.bind(socket_address_rover)
    server_socket.bind(socket_address)
    server_socket_rover.listen(5)
    server_socket.listen(5)
    print("LISTENING AT: " + str(socket_address[0]) + ":" + str(socket_address[1]))
    print("LISTENING AT: " + str(socket_address_rover[0]) + ":" + str(socket_address_rover[1]))
    client_socket_rover, addr = server_socket_rover.accept()
    print("ROVER CONNECTED AT: " + str(addr[0]) + ":" + str(addr[1]))
    client_socket, addr = server_socket.accept()
    print("COMMAND AND CONTROL CONNECTED AT: " + str(addr[0]) + ":" + str(addr[1]))
    controll_to_rover_process = Process(target=controll_to_rover, args=(client_socket,client_socket_rover,))
    rover_to_controll_process = Process(target=rover_to_controll, args=(client_socket,client_socket_rover,))
    controll_to_rover_process.start()
    rover_to_controll_process.start()