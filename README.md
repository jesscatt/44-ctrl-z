# 🤠 Sistema de Rodeio com IA e Informações Integradas

Este é um projeto de sistema integrado para gerenciamento de rodeios, com uso de Inteligência Artificial para análises e automações. Desenvolvido para ser leve, funcional e sem uso de HTML/CSS, voltado para interface via terminal ou APIs.

## 🚀 Funcionalidades

- 🎯 Cadastro de participantes, animais e provas
- 📊 Painel de informações em tempo real
- 🧠 Módulo de IA para:
  - Previsão de pontuações
  - Análise de desempenho
  - Sugestões automáticas de estratégias
- 🔄 API para integração com outros sistemas
- 📂 Banco de dados interno para histórico de eventos e resultados

## 🛠️ Tecnologias Utilizadas

- `Python` para lógica e IA
- `FastAPI` para criação da API
- `SQLite` como banco de dados leve
- `Pandas` e `scikit-learn` para processamento e aprendizado de máquina

## 📦 Como executar

```bash
# Clone o repositório
git clone https://github.com/SeuUsuario/nome-do-repositorio.git

# Acesse a pasta
cd nome-do-repositorio

# Instale as dependências
pip install -r requirements.txt

# Execute a API
uvicorn main:app --reload
