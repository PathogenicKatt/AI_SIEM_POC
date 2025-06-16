from log_collector import typical_log_generator
from log_parser import parse_ssh_log
from rule_detection import RuleDetection
from alerting import send_alert
import time


Discord_webhook_url = "https://discord.com/api/webhooks/1384165307379224576/EX-WJqbFbNil_-tSVyAOQ8AKL9o2vasR8F09G4PWrSXzCZ9nM8__WIbh0YNQxcF8x_DB"

def main():
    rule_detection = RuleDetection()

    while True:
        log_entry = typical_log_generator()
        parsed_log = parse_ssh_log(log_entry)

        if parsed_log and rule_detection.detect_brute_force(parsed_log):
            alert_msg = (
                f"**Brute Force Attack Detected!**\n"
                f"- IP: {parsed_log['ip']}\n"
                f"- User: {parsed_log['user']}\n"
                f"- Time: {parsed_log['timestamp']}\n"
            )
            send_alert(alert_msg, Discord_webhook_url)
        
        time.sleep(1)  # Sleep for a second before generating the next log entry

if __name__ == "__main__":
    main()
