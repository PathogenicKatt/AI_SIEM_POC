import re

def parse_ssh_log(line):
    pattern = r"(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (\S+) sshd.*(failed|accepted).*user (\w+)"
    match = re.search(pattern,line)
    if match:
        return {
            "timestamp": match.group(1),
            "host": match.group(2),
            "action": match.group(3),
            "user": match.group(4)
        }
    return None