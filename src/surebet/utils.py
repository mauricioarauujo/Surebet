import pandas as pd
import logging

logger = logging.getLogger(__name__)


def get_game_ids(all_odds_df: pd.DataFrame) -> list:
    """Retorna os game_ids em comuns dos scrapers.

    Args:
        all_odds_df (pd.DataFrame): dataframe de odds

    Returns:
        list: game_ids
    """

    game_ids = all_odds_df.value_counts('game_id')
    game_ids = game_ids[game_ids>1].index

    return list(game_ids)


def get_prob_values(all_odds_df: pd.DataFrame, empate: bool = True) -> pd.DataFrame:
    """Retorna os valores de probalidade para o surebet.

    Args:
        all_odds_df (pd.DataFrame): Scrapers
        empate (bool): Caso ha possibildiade de empate

    Returns:
        pd.DataFrame: Dataframe com game_id, prob_value
    """
    logger.info('Getting Prob Values for Surebet...')

    game_ids = get_game_ids(all_odds_df)

    prob_df = pd.DataFrame()

    for game_id in game_ids:

        df_game = all_odds_df.query('game_id == @game_id')

        max_odd_mandante = (
            df_game
            .nlargest(1, 'odd_mandante')
            .iloc[0]['odd_mandante']
        )
        max_odd_visitante = (
            df_game
            .nlargest(1, 'odd_visitante')
            .iloc[0]['odd_visitante']
        )
        if empate:
            max_odd_empate = (
                df_game
                .nlargest(1, 'odd_empate')
                .iloc[0]['odd_empate']
            )

        max_odd_mandante_casa = (
            df_game
            .nlargest(1, 'odd_mandante')
            .iloc[0]['casa_de_aposta']
        )
        max_odd_visitante_casa = (
            df_game
            .nlargest(1, 'odd_visitante')
            .iloc[0]['casa_de_aposta']
        )
        if empate:
            max_odd_empate_casa = (
                df_game
                .nlargest(1, 'odd_empate')
                .iloc[0]['casa_de_aposta']
            )

        prob_mandante = 1/max_odd_mandante
        prob_visitante = 1/max_odd_visitante
        total_prob_value = prob_mandante + prob_visitante
        if empate:
            prob_empate = 1/max_odd_empate
            total_prob_value = total_prob_value + prob_empate

        game_prob_df = pd.DataFrame({
            'game_id': [game_id],
            'total_prob_value': [total_prob_value],
            'mandante': [df_game['mandante'].values[0]],
            'max_odd_mandante': [max_odd_mandante],
            'prob_mandante': [prob_mandante],
            'max_odd_mandante_casa': [max_odd_mandante_casa],
            'max_odd_visitante': [max_odd_visitante],
            'prob_visitante': [prob_visitante],
            'max_odd_visitante_casa': [max_odd_visitante_casa]
        })
        if empate:
            game_prob_df['max_odd_empate'] = max_odd_empate
            game_prob_df['prob_empate'] = prob_empate
            game_prob_df['max_odd_empate_casa'] = max_odd_empate_casa

        prob_df = pd.concat([prob_df, game_prob_df])

    prob_df = (
        prob_df
        .sort_values(by=['total_prob_value'])
    )

    return prob_df
