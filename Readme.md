# Projeto Segunda

Inicio da elaboração do assistente virtual Segunda

## Pré requisitos

Para iniciar o projeto é necessario ativar e configurar o ambiente virtual com os seguintes comandos:

```
python -m venv venv
```

Inicializar o ambiente com o seguinte comando:

```
venv\scripts\activate
```

Instalar as dependencias presentes dentro do `requirements.txt`:

```
pip install -r requirements.txt
```

## Preparando o modelo de IA basica para o projeto

Para preparar o modelo de IA é necessario seguir os seguintes passos:

### 1 - Acessar a pasta `AI` e calibrar seu arquivo `train.py`
Defina as variaveis `batch_size` e `hidden_size`, de acordo com suas preferencias
```
num_epochs = 1000
batch_size = 8
learning_rate = 0.0001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)
```

### 2 - Executar o arquivo `train.py`

Antes de iniciar o treino, precisa prepara o nltk com os seguintes comandos
```
Python
```
```
>> import nltk
>> nltk.download('punkt')
```
```
python train.py
```

## Steps do projeto

Por se o inicio do desenvolvimento, há desafios funcionalidades e libs a serem implementadas.

- [X] Iniciar projeto

- [ ] Definir proximos passos

- [X] Preparar IA dedicada localmente