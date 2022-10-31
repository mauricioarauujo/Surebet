"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from surebet.pipelines import futebol_br_seria_a as br_serie_a


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """

    return {
        "__default__": br_serie_a.create_pipeline(),
        "br_serie_a": br_serie_a.create_pipeline()
    }
