from collections import defaultdict

class RuleDetection:
    def __init__(self):
        self.failed_logins = defaultdict(int) # Dictionary to count failed logins per user or IP
    
    def detect_brute_force(self, log):
        if "failed" in log["raw"].lower():
            self.failed_logins[log["ip"]] += 1
            if self.failed_logins[log["ip"]] > 3:  # Lowered from 6 to 3 for demo
                return True
        return False
