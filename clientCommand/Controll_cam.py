import socket, cv2, pickle, struct
def run():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = "tntdns.ddns.net"
        port = 6969
        client_socket.connect((host_ip, port))
        print("Connected to server!")
        data = b''
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = client_socket.recv(4096)
                if not packet: break
                data += packet
            packet_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packet_msg_size)[0]
            while len(data) < msg_size:
                data += client_socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("Recived", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
        client_socket.close()
    except Exception as x:
        print("Error:")
        print(x)
        client_socket.close()

if __name__ == '__main__':
    while True:
        run()