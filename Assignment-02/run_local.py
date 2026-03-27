"""
run_local.py – Execute KFP pipeline components directly as Python functions.

Each component is called via its .python_func attribute, skipping the KFP
runner entirely.  This is the simplest way to run and demo the pipelines
without any Kubernetes or Docker infrastructure.

Usage:
    pip install scikit-learn kfp --break-system-packages
    python3 run_local.py
"""

from hello_pipeline import say_hello
from iris_pipeline import load_data, train_model


def run_hello_world():
    print("─" * 50)
    print("Pipeline 1: hello-world-pipeline")
    print("─" * 50)

    greeting = say_hello.python_func(name="ML-Ops Team")
    print(f"Output → {greeting}")


def run_iris_classification():
    print("─" * 50)
    print("Pipeline 2: iris-classification-pipeline")
    print("─" * 50)

    # Step 1 – load data
    print("\nStep 1: load-data")
    features, labels = load_data.python_func()
    print(f"  Loaded {len(features)} samples, "
          f"{len(features[0])} features")

    # Step 2 – train model
    print("\nStep 2: train-model")
    accuracy, = train_model.python_func(
        features=features,
        labels=labels,
    )
    print(f"  Accuracy → {accuracy:.4f}")


def main():
    print("=" * 50)
    print("  ML-Ops Assignment 2 – KFP Pipeline Demo")
    print("=" * 50)
    print()

    run_hello_world()
    print()
    run_iris_classification()

    print()
    print("=" * 50)
    print("  All pipelines completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
