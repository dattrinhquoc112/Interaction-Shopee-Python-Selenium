import re
import subprocess

def getCurrentMac():
    output = subprocess.check_output(["ifconfig " + "wlan0"], shell= True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    return current_mac.group(0)

def changeCurrentMac(newMac: str):
    subprocess.call(["ifconfig wlan0 hw ether " + newMac], shell=True)
