import socket
def scanner(target, start, end):
    print(f"Scanning port {start} to {end} of {target}")

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    ip_adress = input("Enter your IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    scanner(ip_adress, start_port, end_port)
