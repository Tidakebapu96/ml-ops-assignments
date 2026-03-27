from kfp import dsl, compiler


@dsl.component(base_image="python:3.9-slim")
def say_hello(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting


@dsl.pipeline(name="hello-world-pipeline")
def hello_pipeline(recipient: str = "World"):
    say_hello(name=recipient)


if __name__ == "__main__":
    compiler.Compiler().compile(hello_pipeline, "hello_world_pipeline.yaml")
    print("Compiled: hello_world_pipeline.yaml")