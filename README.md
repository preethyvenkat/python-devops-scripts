#Python DevOps Toolkit

A collection of real-world DevOps automation scripts written in Python. These tools are designed to enhance operational visibility, automate monitoring, and support alerting pipelines in cloud-native environments like AWS and Kubernetes.

## Tools

| Script | Description |
|--------|-------------|
| `elk_index_cleanup.py` | Automates cleanup of old Elasticsearch indices and triggers snapshot |
| `eks_targetgroup_healthcheck.py` | Checks health of targets in AWS ELB Target Groups |
| `k8s_probe_check.py` | Scans Kubernetes deployments for missing readiness/liveness probes |
| `slack_alerts.py` | Sends messages or alerts to Slack via webhook |

##Requirements

- Python 3.8+
- `boto3`, `requests`, `kubernetes`, `flake8`

## Usage

```bash
python elk_index_cleanup.py --days 7 --host http://localhost:9200
python eks_targetgroup_healthcheck.py --region us-west-2 --target-group <TG_ARN>
python k8s_probe_check.py --namespace prod
python slack_alerts.py --message "Unhealthy target detected" --webhook-url <URL>
```

## 🔁 CI/CD

Includes GitHub Actions workflow for linting and static checks on every push.
