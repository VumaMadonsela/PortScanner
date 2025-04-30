import socket
import sys

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            print("Socket error")
            break

    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

def main():
    try:
        ip = input("Enter the IP address to scan: ")
        socket.inet_aton(ip)

        start_port = int(input("Enter start port (e.g. 20): "))
        end_port = int(input("Enter end port (e.g. 80): "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("❌ Invalid port range.")
            sys.exit()

        scan_ports(ip, start_port, end_port)

    except socket.error:
        print("❌ Invalid IP address.")
    except ValueError:
        print("❌ Please enter valid numbers for ports.")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")

if __name__ == "__main__":
    main()

