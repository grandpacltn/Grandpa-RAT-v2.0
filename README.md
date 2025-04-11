# Grandpa RAT v2.0 - Phase 1

## Features
- Reverse Shell
- Screenshot & Webcam Capture
- Keylogger
- ASCII Banner Branding
- Basic Auth Protection

## How to Use

1. Install dependencies:
```bash
pip install pyautogui opencv-python pynput
```

2. Start the server:
```bash
python server/rat_server.py
```

3. Run the client on the victim system:
```bash
python client/rat_client.py
```

4. Available commands:
- `screenshot`
- `webcam`
- `cd <directory>`
- Any shell command (e.g., `dir`, `ls`, `ipconfig`)
- `exit`

> Tested locally. Use in a virtual lab environment only.