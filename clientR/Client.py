import socket, cv2, pickle, struct
def run():
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_ip = "tntdns.ddns.net"
            port = 6970
            client_socket.connect((host_ip, port))
            print("Connected to server!")
            while True:
                if client_socket:
                    vid = cv2.VideoCapture(0)
                    while (vid.isOpened()):
                        img, frame = vid.read()
                        a = pickle.dumps(frame)
                        message = struct.pack("Q", len(a)) + a
                        client_socket.send(message)
                        cv2.imshow("TRANSMITTING VIDEO", frame)
                        key = cv2.waitKey(1) & 0xFF
                        if key == ord("q"):
                            client_socket.close()
        except Exception as x:
            print("Error:")
            print(x)
            client_socket.close()

if __name__ == '__main__':
    run()