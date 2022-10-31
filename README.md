# Surebet

Projeto com intuito de treinar web scrapping. Para diferentes casas de apostas são retiradas as odds para determinadas partidas através de um web scraping. A partir destas diferentes odds é verificada a existência de uma "surebet" que é quando tais odds te garantem um retorno positivo indepedente do resultado.

### Setup

Tal projeto fará uso do Selenium, logo, é necessário instalar tanto o Selenium quanto seus webdrivers.

Segue o link para tutorial: https://selenium-python.readthedocs.io/installation.html

Será necessário também um gerenciador de ambiente. No exemplo abaixo é utilizado o conda mas pode ser qualquer outro de sua escolha.
Exemplo de criação de ambiente com conda:

~~~~~~~~~~~~~~~~~~~~~~~
   (base) $ git clone https://github.com/mauricioarauujo/Surebet.git
   (base) $ conda create -n {env_name} python==3.9 
   (base) $ conda activate {env_name} 
   ({env_name}) $ pip install -r requirements.txt
   
~~~~~~~~~~~~~~~~~~~~~~~

### Running

Para rodagem, já existe um ambiente pronto (kedro) onde para rodar o pipeline principal basta rodar em seu terminal:

~~~~~~~~~~~~~~~~~~~~~~~

  ({env_name}) $ kedro run

~~~~~~~~~~~~~~~~~~~~~~~

Para rodagem de outros pipelines basta digitar:

~~~~~~~~~~~~~~~~~~~~~~~

  ({env_name}) $ kedro run -p {nome_do_pipeline}
   
   Ex: # gerar surebets para o futebol brasileiro serie A
   ({env_name}) $ kedro run -p br_serie_a 
   
~~~~~~~~~~~~~~~~~~~~~~~

Tais pipelines estarão em src/surebet/pipeline_registry.py

Os arquivos serão salvos localmente em suas devidas camadas (raw, output, etc.) dentro do diretório data/.
