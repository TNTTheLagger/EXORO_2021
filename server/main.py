import relay_server

if __name__ == '__main__':
    while True:
        try:
            relay_server.run()
        except Exception as x:
            print("Error:")
            print(x)
            relay_server.server_socket_rover.close()
            relay_server.server_socket.close()