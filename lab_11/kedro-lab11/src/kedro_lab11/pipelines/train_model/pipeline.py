"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                split_data,
                ["model_input", "params:split_params"],
                ["x_train", "x_val", "x_test", "y_train", "y_val", "y_test"],
                name="split",
            ),
            node(
                train_model,
                ["x_train", "y_train", "x_val", "y_val"],
                "best_model",
                name="train",
            ),
            node(
                evaluate_model,
                ["best_model", "x_test", "y_test"],
                None,
                name="evaluate",
            ),
        ]
    )
