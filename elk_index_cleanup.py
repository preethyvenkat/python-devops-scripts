import requests
import argparse
from datetime import datetime, timedelta

def cleanup_indices(elk_host, days_old):
    cutoff_date = (datetime.utcnow() - timedelta(days=days_old)).strftime("%Y.%m.%d")
    index_pattern = f"logstash-{cutoff_date}"
    delete_url = f"{elk_host}/{index_pattern}"
    res = requests.delete(delete_url)
    print(f"Deleted indices older than {days_old} days: {res.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, help="Elasticsearch host")
    parser.add_argument("--days", type=int, default=7, help="Days to keep")
    args = parser.parse_args()
    cleanup_indices(args.host, args.days)
