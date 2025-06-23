import requests
import argparse

def send_alert(message, webhook_url):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    print(f"Slack response: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", required=True, help="Alert message")
    parser.add_argument("--webhook-url", required=True, help="Slack webhook URL")
    args = parser.parse_args()
    send_alert(args.message, args.webhook_url)
