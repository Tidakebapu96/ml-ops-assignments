#!/bin/bash
# =============================================================
# deploy.sh  –  Build & deploy to local Minikube
# =============================================================
# Prerequisites:
#   1. minikube start
#   2. kubectl configured to use minikube context
# =============================================================

set -e

APP_NAME="kidney-disease-classifier"
NAMESPACE="ml-ops"

echo "========================================"
echo " ML-Ops Assignment – Minikube Deploy"
echo "========================================"

# Step 1: Point local Docker CLI at Minikube's Docker daemon
# This means the image will be built INSIDE Minikube so K8s can use it
echo ""
echo "[1/4] Switching Docker context to Minikube..."
eval $(minikube docker-env)

# Step 2: Build the Docker image
echo ""
echo "[2/4] Building Docker image: ${APP_NAME}:latest"
docker build -t ${APP_NAME}:latest .

# Step 3: Apply Kubernetes manifests
echo ""
echo "[3/4] Applying Kubernetes manifests..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Step 4: Wait for rollout & start port-forward
echo ""
echo "[4/4] Waiting for deployment to become ready..."
kubectl rollout status deployment/${APP_NAME} -n ${NAMESPACE} --timeout=120s

# On Linux with Docker driver, NodePort is not directly reachable.
# Port-forward the service to localhost:8080 instead.
echo ""
echo "Starting port-forward: http://localhost:8080  →  pod:8080"
echo "(Keep this terminal open, or run in background with: kubectl port-forward svc/${APP_NAME}-svc -n ${NAMESPACE} 8080:80 &)"
echo ""
kubectl port-forward svc/${APP_NAME}-svc -n ${NAMESPACE} 8080:80 --address=0.0.0.0
