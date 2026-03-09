import socket

def run_scanner(target, ports):
    print(f"\n--- Scanning {target} ---")
    for port in ports:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Fast scanning
        
        # Returns 0 if connection is successful
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()