# Surebet

Projeto para procurar por surebets em diferentes casas de apostas. Para diferentes casas de apostas são retiradas as odds para determinadas partidas através de um web scraping. A partir destas diferentes odds é verificada a existência de uma "surebet" que é quando tais odds te garantem um retorno positivo indepedente do resultado.

### Setup

Tal projeto fará uso do Selenium, logo, é necessário instalar tanto o Selenium quanto seus webdrivers.

Segue o link para tutorial: https://selenium-python.readthedocs.io/installation.html

Será necessário também um gerenciador de ambiente. No exemplo abaixo é utilizado o conda mas pode ser qualquer outro de sua escolha.
Exemplo de criação de ambiente com conda:

~~~~~~~~~~~~~~~~~~~~~~~
   (base) $ git clone https://github.com/mauricioarauujo/Surebet.git
   (base) $ conda create -n {env_name} python==3.9.13
   (base) $ conda activate {env_name} 
   ({env_name}) $ pip install -r requirements.txt
   
~~~~~~~~~~~~~~~~~~~~~~~

### Running

Para rodagem, já existe um ambiente pronto (kedro). Para rodar o pipeline principal, por exemplo, basta digitar em seu terminal:

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

### Outputs

Os arquivos serão salvos localmente em suas devidas camadas (raw, output, etc.) dentro do diretório data/.

Exemplo de output para a Serie A do Futebol Brasileiro:

![image](https://user-images.githubusercontent.com/58861384/199152651-92f53bed-66d8-4bb1-bef9-5fec1dd4aba4.png)

No campo "total_prob_value", quando há um valor menor que 1, confirmamos a existência de uma surebet. A partir disso avaliamos as outras colunas para saber como prosseguir com tal aposta.
