# Kubeflow Pipelines – ML Ops Assignment 2

Two ML pipelines built with the **Kubeflow Pipelines (KFP) v2 SDK**, deployed locally on Minikube.

---

## Pipelines

### 1. Hello World Pipeline (`hello_pipeline.py`)
A minimal KFP pipeline that takes a name as input and returns a greeting string. Used to verify KFP is working correctly on the cluster.

### 2. Iris Classification Pipeline (`iris_pipeline.py`)
An end-to-end ML pipeline with two steps:
- **load_data** — loads the Iris dataset from scikit-learn
- **train_model** — trains a Random Forest classifier and prints accuracy

---

## Project Structure

```
Assignment-02/
├── hello_pipeline.py          ← Hello World KFP pipeline
├── hello_world_pipeline.yaml  ← Compiled KFP spec (upload to UI)
├── iris_pipeline.py           ← Iris classification KFP pipeline
├── iris_pipeline.yaml         ← Compiled KFP spec (upload to UI)
├── deploy.sh                  ← One-command Minikube + KFP setup
└── README.md
```

---

## Local Setup (compile pipelines only)

```bash
pip install kfp scikit-learn

# Recompile pipeline YAMLs (only needed if you change the .py files)
python hello_pipeline.py
python iris_pipeline.py
```

---

## Minikube Deployment

### Prerequisites

| Tool | Install |
|---|---|
| Minikube | `curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && sudo install minikube-linux-amd64 /usr/local/bin/minikube` |
| kubectl | `sudo apt-get install -y kubectl` |
| kfp SDK | `pip install kfp` |

### Deploy with one command

```bash
chmod +x deploy.sh
./deploy.sh
```

The script:
1. Starts Minikube with enough resources for KFP
2. Installs Kubeflow Pipelines standalone on the cluster
3. Waits for all pods to be ready
4. Starts port-forward so the KFP UI is accessible at **http://localhost:8080**

### Upload pipelines

Once the UI is open at http://localhost:8080:

1. Go to **Pipelines → Upload pipeline**
2. Upload `hello_world_pipeline.yaml` → create a run
3. Upload `iris_pipeline.yaml` → create a run

### Or upload via CLI

```bash
pip install kfp
python -c "
import kfp
client = kfp.Client(host='http://localhost:8080')
client.upload_pipeline('hello_world_pipeline.yaml', pipeline_name='Hello World')
client.upload_pipeline('iris_pipeline.yaml', pipeline_name='Iris Classification')
"
```

### Useful commands

```bash
# Check all KFP pods
kubectl get pods -n kubeflow

# Stream logs from a pod
kubectl logs -f -n kubeflow <pod-name>

# Stop port-forward and delete everything
kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=2.3.0"
minikube stop
```
