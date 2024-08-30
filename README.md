# oasis_alert
By mimicking multiple suspicious activities such as failed login attempts, file modifications, port scanning, command execution, and registry manipulation, the Oasis Alert tool aims to simulate scenarios where SOC teams experience alert fatigue due to the overwhelming volume of benign-looking but suspicious alerts.

Installation
Prerequisites
Python 3.x is required to run the tool.
The tool is designed for Windows systems, as it leverages Windows-specific APIs.

Dependencies
The tool uses built-in Python libraries such as ctypes, os, socket, and threading. No external packages need to be installed.

Run the tool using Python:

      python oasis_alert.py
