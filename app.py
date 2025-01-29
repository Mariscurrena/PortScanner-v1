import pyfiglet ## Banner
import sys ## Manage system
import socket ## Ports
from datetime import datetime ## Logs
import os

## Port Scanner Banner
os.system("cls")
ascii_banner = pyfiglet.figlet_format("PORT SCANNER V1")
print(f"\033[1;32m{ascii_banner}\033[0m")

# ¡Idea: In future version, make this able to received a list or a file text and make the scanner function recursive, in order to be able to perform scans to multiple targets
target = input(str("Target IP: "))
bport = input("Specify the port number where the scan will begin: ")
eport = input("Specify the port number where the scan will end: ")

# Banner and logs of the scan
print("\033[34m-\033[0m" * 70 + "\n")
print(f"\033[34mScanning Target: {target}\033[0m")
print(f"\033[34mScanning started at: {str(datetime.now())}\033[0m")
print("\033[34m-\033[0m" * 70 + "\n")

# Script to detects all ports into the server
try:
    # Scan every port
    for port in range(int(bport),int(eport)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Return open port
        result = s.connect_ex((target,port))
        if result == 0: # Zero means successfull connection
            print("[*] Port{} is open".format(port))
        s.close()
    print("\033[34m-\033[0m" * 70 + "\n")
    print(f"\033[32m[//] Target Scan {target} completed!\033[0m")
    print(f"\033[34mScan ended at: {str(datetime.now())}\033[0m")
    print("\033[34m-\033[0m" * 70 + "\n")

# Adding exceptions
except KeyboardInterrupt:
    print("\033[31m-\033[0m" * 70)
    print("\033[31m[X] Manual Cancelation!\033[0m")
    print("\033[31m[X] Exiting!\033[0m")
    print("\033[31m-\033[0m" * 70)
    sys.exit()
except socket.error:
    print("\033[31m-\033[0m" * 70)
    print("\033[31m[X] Host not responding!\033[0m")
    print("\033[31m-\033[0m" * 70)
    sys.exit()