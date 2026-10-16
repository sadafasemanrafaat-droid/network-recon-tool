import socket
import time

host = input("Enter Target: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("----------------")
print("NETWORK RECON TOOL")
print("----------------")

start_time = time.time()  # start timing AFTER the user input


def scan_port(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1000)
            try:
                s.connect((host, port))
                open_ports.append(port)
            except (socket.timeout, socket.error):
                pass

    return open_ports


def scanner_http(host, port):
    """Returns (service, banner)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1000)
        try:
            s.connect((host, port))

            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"Connection: close\r\n"
                f"\r\n"
            )
            s.sendall(request.encode())

            response = s.recv(4096)
            text = response.decode(errors="ignore")

            # A real HTTP response starts with "HTTP/"
            if text.startswith("HTTP/"):
                banner = "Not found"
                for line in text.splitlines():
                    if line.lower().startswith("server:"):
                        banner = line.strip()
                        break
                return "HTTP", banner

            return "Not recognized", "None"

        except (socket.timeout, socket.error):
            return "Not recognized", "None"


# Scan ports
open_ports = scan_port(host, start_port, end_port)

print(f"Open ports: {open_ports}")

for port in open_ports:
    service, banner = scanner_http(host, port)
    print(f"Port {port} -> Service: {service}")
    print(f"Banner: {banner}")

total_time = time.time() - start_time
print(f"Scan Time: {total_time:.2f} seconds")
print("----------------")