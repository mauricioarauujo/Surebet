from selenium.webdriver import Firefox, FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
from unidecode import unidecode
import pandas as pd
import numpy as np

def get_betway_odds_br_serie_a():
    
    opts = FirefoxOptions()
    opts.headless = True
    browser = Firefox(options=opts)
    browser.implicitly_wait(2)

    browser.get('https://betway.com/pt/sports/grp/soccer/brazil/brasileiro-serie-a')
    
    base_xpath = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div'

    games_ids = []

    mandantes = []
    visitantes = []

    odds_mandantes = []
    odds_empates = []
    odds_visitantes = []

    for day in range(1,5):
        for game in range(1,20):
            try:
                text_game = browser.find_element(
                    by='xpath',
                    value = base_xpath + f'/div[{day}]/div[2]/div/div[{game}]'
                ).text

                _, game_name, odd_mandante, odd_empate, odd_visitante = text_game.split('\n')
                clubs = [unidecode(club.strip()).lower().replace(' ', '_') for club in game_name.split('-')]
                game_id = '-'.join(sorted(clubs))
                mandante = clubs[0]
                visitante = clubs[1]



                games_ids.append(game_id)
                mandantes.append(mandante)
                visitantes.append(visitante)
                odds_mandantes.append(float(odd_mandante.replace(',', '.')))
                odds_empates.append(float(odd_empate.replace(',', '.')))
                odds_visitantes.append(float(odd_visitante.replace(',', '.')))
            except NoSuchElementException:
                break
    df = pd.DataFrame({
        'game_id': games_ids,
        'mandante': mandantes,
        'visitante': visitantes,
        'odd_mandante': odds_mandantes,
        'odd_empate': odds_empates,
        'odd_visitante': odds_visitantes
    })
    df['casa_de_aposta'] = 'Betway'
    browser.quit()
    
    return df

def get_sporting_bet_odds_br_serie_a():
    
    clubs_map = {
        'fluminense_fc_rj': 'fluminense',
        'ceara_sc': 'ceara',
        'botafogo_fr_rj': 'botafogo',
        'cuiaba_esporte_clube_mt': 'cuiaba',
        'atletico_mineiro_mg': 'atletico_mineiro',
        'coritiba_fc_pr': 'coritiba',
        'sao_paulo_fc_sp': 'sao_paulo',
        'ca_paranaense_pr': 'athletico_pr',
        'ec_juventude_rs': 'juventude',
        'america_mg': 'america_mineiro',
        'sc_internacional_rs': 'internacional',
        'goias_ec_go': 'goias',
        'ac_goianiense_go': 'atletico_goianiense',
        'santos_fc_sp': 'santos',
        'avai_fc_sc': 'avai',
        'red_bull_bragantino': 'bragantino',
        'cr_flamengo_rj': 'flamengo',
        'sc_corinthians_sp': 'corinthians',
        'fortaleza_ec_ce': 'fortaleza',
        'se_palmeiras_sp': 'palmeiras'
    }
    
    opts = FirefoxOptions()
    opts.headless = True
    browser = Firefox(options=opts)
    browser.implicitly_wait(2)

    browser.get('https://sports.sportingbet.com/en/sports/football-4/betting/brazil-33/brasileiro-serie-a-102838')
    
    base_xpath = '//*[@id="main-view"]/ms-widget-layout/ms-widget-slot/ms-composable-widget/ms-widget-slot[2]/ms-tabbed-grid-widget/ms-grid/div'

    games_ids = []

    mandantes = []
    visitantes = []

    odds_mandantes = []
    odds_empates = []
    odds_visitantes = []

    for day in range(1,5):
        for game in range(1,10):
            try:
                text_game = browser.find_element(
                    by='xpath',
                    value = base_xpath + f'/ms-event-group[{day}]/ms-event[{game}]/div'
                ).text
                
                if len(text_game.split('\n')) == 10:
                    mandante, visitante, _, _, odd_mandante, odd_empate, odd_visitante, _, _, _ = text_game.split('\n')
                elif len(text_game.split('\n')) == 9:
                    mandante, visitante, _, odd_mandante, odd_empate, odd_visitante, _, _, _ = text_game.split('\n')
                elif len(text_game.split('\n')) == 8:
                    mandante, visitante, odd_mandante, odd_empate, odd_visitante, _, _, _ = text_game.split('\n')
                else: 
                    raise NoSuchElementException()

                clubs = [unidecode(club.strip()).lower().replace(' ', '_') for club in [mandante.strip(), visitante.strip()]]
                clubs = [clubs_map[club] if club in clubs_map.keys() else club for club in clubs]
                game_id = '-'.join(sorted(clubs))
                
                mandante = clubs[0]
                visitante = clubs[1]

                games_ids.append(game_id)
                mandantes.append(mandante)
                visitantes.append(visitante)
                odds_mandantes.append(float(odd_mandante))
                odds_empates.append(float(odd_empate))
                odds_visitantes.append(float(odd_visitante))
            
            except NoSuchElementException:
                break
            
    df = pd.DataFrame({
        'game_id': games_ids,
        'mandante': mandantes,
        'visitante': visitantes,
        'odd_mandante': odds_mandantes,
        'odd_empate': odds_empates,
        'odd_visitante': odds_visitantes
    })
    df['casa_de_aposta'] = 'Sportingbet'
    browser.quit()
    
    return df