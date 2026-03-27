# Kidney Disease Classification – ML Ops Assignment

CNN-based deep learning project that classifies kidney CT scans as **Tumor** or **Normal**.
Built with TensorFlow / VGG-16, served via Flask, tracked with MLflow, and pipelined with DVC.

---

## Project Structure

```
app.py               ← Flask web server (predict + train endpoints)
main.py              ← Full training pipeline runner
Dockerfile           ← Container image definition
dvc.yaml             ← DVC pipeline stages
params.yaml          ← Model hyper-parameters
requirements.txt     ← Python dependencies
k8s/                 ← Kubernetes manifests for Minikube
  namespace.yaml
  deployment.yaml
  service.yaml
deploy.sh            ← One-command Minikube deploy script
src/cnnClassifier/   ← Core package
  components/        ← Data ingestion, model prep, training, evaluation
  config/            ← Config manager
  pipeline/          ← Stage pipelines + prediction
  utils/             ← Helpers (YAML reader, dir creator, …)
templates/           ← Flask HTML frontend
```

---

## Workflows (development order)

1. Update `config/config.yaml`
2. Update `params.yaml`
3. Update entity (`src/cnnClassifier/entity/config_entity.py`)
4. Update configuration manager (`src/cnnClassifier/config/configuration.py`)
5. Update components (`src/cnnClassifier/components/`)
6. Update pipeline stages (`src/cnnClassifier/pipeline/`)
7. Update `main.py`
8. Update `dvc.yaml`
9. Update `app.py`

---

## Local Development (without Docker)

```bash
# 1. Clone the repo
git clone https://github.com/Tidakebapu96/ml-ops-assignments.git
cd ml-ops-assignments

# 2. Create and activate a conda environment
conda create -n kidney-clf python=3.8 -y
conda activate kidney-clf

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the training pipeline
python main.py

# 5. Start the Flask app
python app.py
# → Open http://localhost:8080
```

---

## Minikube Deployment (Local Kubernetes)

### Prerequisites

| Tool | Install |
|------|---------|
| Docker | https://docs.docker.com/get-docker/ |
| Minikube | `curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && sudo install minikube-linux-amd64 /usr/local/bin/minikube` |
| kubectl | `sudo apt-get install -y kubectl` or via Minikube: `minikube kubectl` |

### Step-by-step

```bash
# 1. Start Minikube (allocate enough RAM for TensorFlow)
minikube start --memory=4096 --cpus=2

# 2. Run the deploy script (builds image inside Minikube + applies all manifests)
chmod +x deploy.sh
./deploy.sh
```

The script does 4 things automatically:
1. Points your Docker CLI at Minikube's internal Docker daemon  
2. Builds the image **inside** Minikube (no registry needed)  
3. Applies `k8s/namespace.yaml`, `k8s/deployment.yaml`, `k8s/service.yaml`  
4. Prints the URL where the app is reachable  

### Manual steps (if you prefer)

```bash
# Build image inside Minikube
eval $(minikube docker-env)
docker build -t kidney-disease-classifier:latest .

# Apply manifests
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Get the app URL
minikube service kidney-disease-classifier-svc -n ml-ops --url
```

### Useful kubectl commands

```bash
# List pods in the ml-ops namespace
kubectl get pods -n ml-ops

# Stream logs from the running pod
kubectl logs -f -n ml-ops <pod-name>

# Delete everything
kubectl delete -f k8s/
```

---

## MLflow Experiment Tracking

```bash
mlflow ui
# → Open http://localhost:5000
```

---

## DVC Pipeline

```bash
# Reproduce all stages
dvc repro

# Check stage status
dvc status
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web UI |
| GET/POST | `/train` | Trigger full training pipeline |
| POST | `/predict` | Classify a base64-encoded image |

**Predict request body:**
```json
{ "image": "<base64-encoded-image>" }
```


