from kfp import dsl, compiler
from typing import NamedTuple, List


@dsl.component(base_image="python:3.9-slim", packages_to_install=["scikit-learn"])
def load_data() -> NamedTuple("Outputs", [("features", List[List[float]]), ("labels", List[int])]):
    from sklearn.datasets import load_iris
    iris = load_iris()
    print(f"Loaded Iris dataset: {len(iris.data)} samples, {len(iris.feature_names)} features")
    return (iris.data.tolist(), iris.target.tolist())


@dsl.component(base_image="python:3.9-slim", packages_to_install=["scikit-learn"])
def train_model(features: List[List[float]], labels: List[int]) -> NamedTuple("Output", [("accuracy", float)]):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"Model accuracy: {acc:.4f}")
    return (acc,)


@dsl.pipeline(name="iris-classification-pipeline")
def iris_pipeline():
    data = load_data()
    train_model(features=data.outputs["features"], labels=data.outputs["labels"])


if __name__ == "__main__":
    compiler.Compiler().compile(iris_pipeline, "iris_pipeline.yaml")
    print("Compiled: iris_pipeline.yaml")
