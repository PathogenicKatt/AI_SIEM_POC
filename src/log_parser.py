import re
from datetime import datetime

def parse_ssh_log(line):
    pattern = (
        r"(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2})" # Captures "May 10 14:23:45"
        r".*sshd\[\d+\]: " # Matches "sshd[1234]: "
        r"(?:Failed|Accepted) password for " # Matches "Failed" or "Accepted"
        r"(?P<user>\w+) from (?P<ip>\d+.\d+\.\d+\.\d+) " # Captures "root" and "192.168.1.1"
    )
    match = re.search(pattern,line)
    if match:
        return {
            "timestamp": datetime.strptime(match.group("timestamp"), "%b %d %H:%M:%S").isoformat(), 
            "user": match.group("user"),
            "ip": match.group("ip"),
            "raw": line.strip()
        }
    return None