import pyfiglet ## Banner
import sys ## Manage system
import socket ## Ports
from datetime import datetime ## Logs

## Port Scanner Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER V1")
print(ascii_banner)

# ¡Idea: In future version, make this able to received a list or a file text and make the scanner function recursive, in order to be able to perform scans to multiple targets
target = input(str("Target IP: "))

#Banner and logs of the scan
print("-" * 70)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 70)