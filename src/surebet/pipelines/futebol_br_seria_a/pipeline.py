from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import get_br_serie_a_odds, run_br_serie_a


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_br_serie_a_odds,
                inputs=None,
                outputs="br_serie_a_odds_df",
                name="generate_serie_a_odds",
            ),
            node(
                func=run_br_serie_a,
                inputs="br_serie_a_odds_df",
                outputs="br_serie_a_probs_df",
                name="generate_serie_a_probs",
            )
        ],
        namespace="futebol_br_serie_a_pipeline",
        inputs=None,
        outputs=["br_serie_a_odds_df", "br_serie_a_probs_df"],
    )
