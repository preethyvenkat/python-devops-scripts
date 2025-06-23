from kubernetes import client, config
import argparse

def check_probes(namespace):
    config.load_kube_config()
    v1_apps = client.AppsV1Api()
    deployments = v1_apps.list_namespaced_deployment(namespace=namespace)
    for deploy in deployments.items:
        for container in deploy.spec.template.spec.containers:
            name = container.name
            readiness = container.readiness_probe
            liveness = container.liveness_probe
            if not readiness or not liveness:
                print(f"[!] {deploy.metadata.name}/{name} is missing probes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--namespace", default="default", help="K8s namespace")
    args = parser.parse_args()
    check_probes(args.namespace)
