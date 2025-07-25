# 🚀 Projeto ETL com Airflow, Docker e PostgreSQL (com Trigger) 

Este projeto é um pipeline ETL completo que utiliza ferramentas open source para extrair, transformar e carregar dados de uma API pública para um banco PostgreSQL, com orquestração via Apache Airflow.

## 🛠️ Tecnologias usadas

- **Apache Airflow**: Orquestração e agendamento dos workflows ETL 
- **Docker** e **Docker Compose**: Containerização dos serviços para ambiente isolado e reproduzível  
- **PostgreSQL**: Banco de dados relacional para armazenamento dos dados   
- **Trigger PostgreSQL**: Automação de ações no banco após inserção de dados  
- **Python**: Extração, transformação e carga de dados usando requests, pandas e sqlalchemy  

## ⚙️ Funcionalidades

- Pipeline que roda a cada hora (`schedule_interval='@hourly'`) ⏳🕐  
- Extrai cotações financeiras da API [AwesomeAPI](https://economia.awesomeapi.com.br) 💵
- Transforma e arredonda valores das cotações 
- Carrega os dados para uma tabela no PostgreSQL (`cotacao_moedas`)   
- Executa trigger no PostgreSQL para processar dados automaticamente após a carga (exemplo de uso de trigger)  
- Interface web do Airflow para monitorar o pipeline (http://localhost:8081)  
- Interface Adminer para acessar e manipular o banco (http://localhost:8080)  
