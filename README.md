# 📊 Calculadora de Equivalência Percentual

Uma aplicação interativa desenvolvida com [Streamlit](https://streamlit.io) que permite aplicar uma sequência de variações percentuais sobre um valor inicial e calcular a equivalência percentual total.

> Exemplo: `+20%, -10%, +4.5%` sobre um valor `x` → quanto vale no final? Qual seria o percentual único equivalente?

## 🚀 Demonstração

[🔗 Acesse aqui a aplicação online](https://percentage-equivalence-calculator-gmm.streamlit.app/)

## ✨ Funcionalidades

- Inserção de uma sequência de variações percentuais (ex: `20, -10, 4.5`);
- Opção de ignorar o valor inicial e ver apenas a equivalência percentual;
- Cálculo do valor final e do percentual equivalente total;
- Interface responsiva e estilizada com cores indicativas (ganho/perda).

## 🛠️ Tecnologias Utilizadas

- [Python 3.13+](https://www.python.org/)
- [Streamlit 1.44.1](https://streamlit.io)

## 💻 Como usar localmente

1. Clone este repositório:

```bash
git clone https://github.com/GMMGabriel/percentage-equivalence-calculator.git
cd percentage-equivalence-calculator
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
streamlit run app.py
```

## 📦 Deploy

Você pode facilmente hospedar a aplicação usando o Streamlit Cloud:

1. Crie um repositório no GitHub com os arquivos app.py e requirements.txt;

2. Vá para streamlit.io/cloud, conecte sua conta do GitHub e crie um novo app;

3. Escolha seu repositório, branch e o caminho do script (app.py);

4. Clique em Deploy.

## 📄 Licença

Este projeto está licenciado sob a MIT License.

## 👨‍💻 Autor

Desenvolvido com 💜 por Gabriel de Melo Marcondes.