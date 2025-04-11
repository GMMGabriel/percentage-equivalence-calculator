import streamlit as st

st.set_page_config(
  page_title='Calculadora de Equivalência Percentual',
  page_icon=':chart_with_upwards_trend:'
)

def apply_percentage_changes(initial_value: float, rates: tuple[float]) -> float:
  """
  Aplica uma sequência de variações percentuais sobre um valor inicial.
  
  Parâmetros:
  - initial_value ( float ): valor inicial;
  - rates ( tuple[float] ): tupla de percentuais (ex: [10, -5, 3.5]).
  
  Retorna:
  - ( float ) Valor final após todas as variações.
  """
  final_value = initial_value
  for rate in rates:
      final_value *= (1 + rate / 100)
  return round(final_value, 2)

def calculate_equivalent_percentage(initial_value: float, final_value: float) -> float:
  """
  Calcula o percentual equivalente total de variações.
  
  Parâmetros:
  - initial_value ( float ): valor original;
  - final_value ( float ): valor resultante.
  
  Retorna:
  - ( float ) Percentual equivalente (positivo ou negativo), arredondado com 2 casas decimais.
  """
  return round(((final_value / initial_value) - 1) * 100, 2)

def input_rates_processing(input_rates: str) -> tuple[float]:
  """
  Faz a tratativa dos dados de entrada.

  Parâmetros:
  - input_rates ( str ): dados de entrada.

  Retorna:
  - ( tuple[float] ) tupla de percentuais.
  """
  temp = input_rates.strip()
  while '  ' in temp:
    temp = temp.replace('  ', ' ')
  while ',,' in temp:
    temp = temp.replace(',,', ',')
  while '..' in temp:
    temp = temp.replace('..', '.')
  while temp[0] in ('.', ','):
    temp = temp[1:]
  while temp[-1] in ('.', ','):
    temp = temp[:-1]

  return tuple(round(float(r.strip()), 2) for r in temp.split(',')) if temp != '' else ()

def format_value(value: float, round_value: int = 2):
  """
  Formata um valor para o padrão brasileiro.
  
  Parâmetros:
  - value ( float ): valor a ser formatado.
  
  Retorna:
  - ( str ) Valor formatado.
  """
  return str(round(value, round_value)).replace('.', ',')

def switch_color_by_value(value: float) -> str:
  """
  Alterna a cor do texto de acordo com o valor.
  
  Parâmetros:
  - value ( float ): valor.
  
  Retorna:
  - ( str ) Cor do texto.
  """
  return 'red' if value < 0 else 'green' if value > 0 else 'violet'

st.header('Calculadora de Equivalência Percentual')

st.write('---')

container = st.container()

# Não informar um valor inicial
no_initial_value = container.checkbox('Não informar um valor inicial', value=False)

# Informar um valor inicial
initial_value = 1000
if not no_initial_value:
  initial_value = container.number_input('Valor inicial', value=1000.0, min_value=1.0, step=10.0, format='%.2f')

# Informar as variações
temp = container.text_input('Variações (%), separadas por vírgula. Exemplo: 20, -10, 4.5', value='20, -10, 4.5', max_chars=80)
if '%' in temp:
  container.warning(':warning: ATENÇÃO: Não use o sinal de porcentagem (%).')
  exit(0)
try:
  rates = input_rates_processing(temp)
except:
  container.error(':bangbang: Erro ao processar os dados. Verifique se digitou corretamente.')
  exit(0)

# Nenhuma variação informada
if len(rates) == 0:
  container.error('Nenhuma variação informada.')
  exit(0)

# Mostrar as variações
container.markdown('Variações: ' + ' | '.join([':'+switch_color_by_value(x)+'['+format_value(x)+'%]' for x in rates]))

st.write('---')

# Resultados
try:
  final_value = apply_percentage_changes(initial_value, rates)
  equiv = calculate_equivalent_percentage(initial_value, final_value)

  col1, col2 = st.columns([2, 3])
  col1.subheader(':violet[Resultados]')
  col1.metric(
    label='Equivalência',
    value=format_value(final_value) if not no_initial_value else 'Valor N',
    delta=format_value(equiv) + '%',
    delta_color='normal' if equiv != 0 else 'off',
    label_visibility='collapsed'
  )

  col2.subheader(':violet[Valores]')
  if not no_initial_value:
    col2.write(':bar_chart: Valor final: ' + format_value(final_value))
  col2.write(':chart_with_upwards_trend: Percentual equivalente: ' + format_value(equiv) + '%')
except:
  st.error(':bangbang: Erro ao tentar calcular os resultados. Verifique se digitou corretamente.')

# Rodapé
footer="""
<style>
  a:link , a:visited{
    color: #6d28d9;
    background-color: transparent;
    text-decoration: none;
  }

  a:hover,  a:active {
    color: #8b5cf6;
    background-color: transparent;
    text-decoration: none;
  }

  .footer {
    padding: .5rem;
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000;
    color: #fff;
    text-align: center;
  }
  
  .footer p {
    margin: 0;
  }
</style>
<div class="footer">
  <p>Desenvolvido por <a style='display: inline-block; text-align: center;' href="http://github.com/gmmgabriel/" target="_blank">Gabriel de Melo Marcondes</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)