# Surebet

Projeto com intuito de treinar web scrapping. Para diferentes casas de apostas são retiradas as odds para determinadas partidas através de um web scraping. A partir destas diferentes odds é verificada a existência de uma "surebet" que é quando tais odds te garantem um retorno positivo indepedente do resultado.

### Setup

Após instalar qualquer ambiente conda, digite no seu terminal:

~~~~~~~~~~~~~~~~~~~~~~~
   (base) $ git clone https://github.com/mauricioarauujo/Surebet.git
   (base) $ conda create -n {env_name} python==3.8.2
   (base) $ conda activate {env_name} 
   ({env_name}) $ pip install -r requirements.txt
   ({env_name}) $ pip install -e .
   
~~~~~~~~~~~~~~~~~~~~~~~

### Running

Para rodagem, já existe um ambiente pronto ontem basta rodar em seu terminal:

~~~~~~~~~~~~~~~~~~~~~~~

  ({env_name}) $ python run.py task tasks {nome_da_task}

~~~~~~~~~~~~~~~~~~~~~~~

Tais tasks estarão em src/tasks
