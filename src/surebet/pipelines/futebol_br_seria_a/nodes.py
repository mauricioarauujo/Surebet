import pandas as pd


import pandas as pd
import logging

from surebet.pipelines.futebol_br_seria_a.scrapers import (
    get_betway_odds_br_serie_a,
    get_sporting_bet_odds_br_serie_a
)
from surebet.utils import (
    get_prob_values
)

logger = logging.getLogger(__name__)


def get_br_serie_a_odds() -> pd.DataFrame:
    """Retorna os dataframes dos scrappers com as odds.

    Returns:
        pd.DataFrame: Odds do futebol br serie A
    """
    logger.info('Getting BR Serie A Odds...')
    betway_odds_df = get_betway_odds_br_serie_a()
    sporting_bet_df = get_sporting_bet_odds_br_serie_a()

    all_odds_df = (
        pd.concat([
            betway_odds_df,
            sporting_bet_df])
    )

    return all_odds_df


def run_br_serie_a(br_serie_a_odds_df: pd.DataFrame) -> pd.DataFrame:
    """Funcao pricipal para valores do brasileirao.

    Args:
        br_serie_a_odds_df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: Dataset com os valores de probabilidade para a surebet
    """
    logger.info('Running for BR Serie A Football...')
    br_serie_a_odds_df = get_br_serie_a_odds()

    br_serie_a_probs_df = get_prob_values(br_serie_a_odds_df)

    surebet_counts = len(br_serie_a_probs_df.query('total_prob_value < 1'))
    if not surebet_counts:
        min_surebet = br_serie_a_probs_df['total_prob_value'].min().round(4)
        logger.info(f'No surebets founded. Best prob value: {min_surebet}')
    else:
        logger.info(f'SUREBETS FOUNDED! {surebet_counts} surebets.')

    logger.info(br_serie_a_probs_df.nsmallest(3, ['total_prob_value']).loc[:, ['game_id', 'total_prob_value']])

    return br_serie_a_probs_df
