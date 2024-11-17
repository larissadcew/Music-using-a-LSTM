# 🎶 Music Using a LSTM

O projeto **Music Using a LSTM** é uma implementação de uma rede neural do tipo **LSTM** (Long Short-Term Memory) para gerar música. Utilizando técnicas de aprendizado profundo, o modelo é treinado para entender padrões musicais e criar composições originais com base nos dados de músicas fornecidos durante o treinamento.

## 🔧 Funcionalidades

- **Geração Automática de Música**: O modelo LSTM é capaz de gerar notas musicais sequenciais baseadas em um conjunto de dados de treinamento.
- **Treinamento de Modelo**: O modelo é treinado utilizando um conjunto de dados de músicas para aprender padrões e estruturas musicais.
- **Personalização da Composição**: É possível gerar músicas com diferentes estilos e complexidade, com base nos parâmetros fornecidos.
- **Previsão de Notas Musicais**: A rede LSTM prevê as próximas notas com base nas notas anteriores, criando sequências musicais coesas.

## 🖥️ Tecnologias Utilizadas

- **Python**: O código é escrito em Python, utilizando bibliotecas como TensorFlow e Keras para construir a rede LSTM.
- **TensorFlow/Keras**: Usado para criar e treinar o modelo de rede neural.
- **Música como Dados**: O projeto utiliza arquivos de músicas (em formato MIDI ou outro) para treinar o modelo, que aprende a prever as próximas notas.
- **Matplotlib**: Para visualização de resultados e análise de performances.

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é criar uma rede neural LSTM que possa gerar músicas originais a partir de um conjunto de dados de música existente. Esse tipo de rede neural é bem-sucedido na modelagem de sequências temporais, o que a torna ideal para problemas como a geração de música, onde a sequência de notas e acordes é importante.

### Características:

- **Geração de Música**: Após o treinamento, o modelo é capaz de gerar novas músicas sequenciais.
- **Baseado em LSTM**: Utiliza a arquitetura LSTM para aprender padrões temporais complexos em sequências musicais.
- **Interatividade**: O projeto permite que o usuário forneça um estilo de música para gerar composições no mesmo estilo.
- **Treinamento Customizado**: O modelo pode ser treinado com diferentes conjuntos de dados musicais para obter variações no estilo e complexidade da música gerada.

## ⚙️ Como Rodar o Projeto

Para rodar a geração de música com LSTM, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/larissadcew/Music-using-a-LSTM.git
