import re
import uuid

def getCurrentMac():
    macAddress = hex(uuid.getnode()).replace('0x', '')
    return ':'.join(macAddress[i : i + 2] for i in range(0, 11, 2))