import random 
import time 
from datetime import datetime

def typical_log_generator():
    """So this will generate fake ssh auth logs for testing"""
    users = ["root", "admin", "userX", "ubuntu", "fedora"]
    actions = ["login", "logout", "failed_login"]
    ip = f"192.168.1.{random.randint(1, 255)}"

    log_entry = (
        f"{datetime.now().strftime('%b %d %H:%M:%S')}"
        f"sshd[{random.randint(1000, 9999)}]: "
        f"Failed password for {random.choice(users)} from {ip} port 22"
    )

    return log_entry

def main():
    # This will continuously generate logs and write them to a file
    with open("../data/sample_auth.log","a") as f:
        while True:
            log_entry = typical_log_generator()
            f.write(log_entry + "\n")
            time.sleep(random.uniform(0.1, 2.0)) # Sleep between 0.1 and 2 seconds

if __name__ == "__main__":
    main()