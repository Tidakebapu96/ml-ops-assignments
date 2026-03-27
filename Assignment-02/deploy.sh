#!/bin/bash
# =============================================================
# deploy.sh  –  Install Kubeflow Pipelines on local Minikube
# =============================================================
# Prerequisites: minikube, kubectl installed
# KFP version pinned to a stable standalone release
# =============================================================

set -e

KFP_VERSION="2.3.0"

echo "========================================"
echo " ML-Ops Assignment 2 – KFP on Minikube"
echo "========================================"

# Step 1: Start Minikube
echo ""
echo "[1/4] Starting Minikube (8GB RAM, 4 CPUs)..."
minikube start --memory=8192 --cpus=4 --disk-size=30g

# Step 2: Install KFP standalone
echo ""
echo "[2/4] Installing Kubeflow Pipelines ${KFP_VERSION}..."
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=${KFP_VERSION}"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=${KFP_VERSION}"

# Step 3: Wait for pods to be ready
echo ""
echo "[3/4] Waiting for KFP pods to be ready (this may take a few minutes)..."
kubectl wait --for=condition=ready pod --all -n kubeflow --timeout=300s

# Step 4: Port-forward the KFP UI
echo ""
echo "[4/4] Starting port-forward: http://localhost:8080 → KFP UI"
echo ""
echo "========================================"
echo " KFP is ready!"
echo " Open: http://localhost:8080"
echo " Upload hello_world_pipeline.yaml or iris_pipeline.yaml via the UI"
echo "========================================"
echo ""
kubectl port-forward svc/ml-pipeline-ui 8080:80 -n kubeflow --address=0.0.0.0
