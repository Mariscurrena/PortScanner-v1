import pyfiglet ## Banner
import sys ## Manage system
import socket ## Ports
from datetime import datetime ## Logs

## Port Scanner Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER V1")
print(ascii_banner)

# ¡Idea: In future version, make this able to received a list or a file text and make the scanner function recursive, in order to be able to perform scans to multiple targets
target = input(str("Target IP: "))

# Banner and logs of the scan
print("-" * 70)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 70)

# Script to detects all ports into the server
try:
    # Scan every port
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Return open port
        result = s.connect_ex((target,port))
        if result == 0: # Zero means successfull connection
            print("[*] Port{} is open".format(port))
        s.close()
    print("-" * 70)
    print(f"[//] Target Scan {target} completed!")

# Adding exceptions
except KeyboardInterrupt:
    print("-" * 70)
    print(f"[X] Exiting!")
    sys.exit()
except socket.error:
    print("-" * 70)
    print(f"[X] Host not responding!")
    sys.exit()