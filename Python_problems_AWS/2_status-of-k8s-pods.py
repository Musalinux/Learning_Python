"""
We can use the kubernetes python library to interact with K8s cluster
"""
from kubernetes import config, client

def status_of_pod(namespace, pod_name):
    config.load_kube_config() # LoadK8s config from default location
    v1 = client.CoreV1Api # Create instance of CoreV1Api class
    pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace) # Fetch pod details
    return pod.status.phase # return pod status/phase 

namespace = 'default'
pod_name = 'my-pod'
status = status_of_pod(namespace, pod_name)
print (f"Pod Status is {status}")