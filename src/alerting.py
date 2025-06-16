import requests
import json

def send_alert(message, webhook_url):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers=headers,
            timeout=10  # seconds
        )
        return response.status_code == 204
    except requests.exceptions.RequestException as e:
        print(f"Failed to send alert: {e}")
        return False
    