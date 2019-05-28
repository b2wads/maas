# Math as a (µ)service - MaaS

A ideia desse exercício é mostrar com seria uma arquitetura simples de micro-serviços.

Aqui faremos uma calculadora simples que faz o parsing de uma expressão matemática e no momento
de avaliar essa expressão (para obter o resultado) delega cada operação matemática (+, -, *, /, ) para um serviço separado.

## Operações suportadas

O parser é bem simples e suporta:

 - Mais (+)
 - Menos (-)
 - Divisão (/)
 - Multiplicação (*)
 - Parênteses ()
 - Potência (^)


A implementação do parser é essa: https://github.com/PeterBeard/math-trees


### Exemplo de uma expressão válida

```
3 + 5 * (7^2)
```

# Bugs no Parser

O parser que achamos possui bugs que não vamos resolver, pelo menos por enquanto. Alguns exemplos de expressões que retornam um resultado errado:

 - `1 + 3 + 5 * (7^2)` retorna `248` mas deveria retornar `249`;
 - `8 + 2 - 10` retorna `2` e deveria retornar `0`;

Vamos usar o que pudermos desse parser para podermos fazer o exercício de micro-serviço.



# Como instalar o projeto

Para usar o projeto você precisará de:

 - python 3.7
 - pyenv
 - pipenv

## Instalando o pyenv

Faça o clone do código:
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

adicione em seu bashrc (`~/.bashrc`):

```
export PYENV_ROOT="$HOME/.pyenv
export PATH="$PYENV_ROOT/bin:~/.local/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

## Conferindo a instalação.

Depois de fazer essa instalação, abra um novo terminal e digite:

```
pyenv --version
pyenv 1.2.9-19-g7d02b246
```

Algo parecido com isso deve ser retornado.

## Instalando python 3.7

Para instalar, rode:

```
pyenv install 3.7.2
```

## Ativando o python 3.7

Para escolher o python com interpretador default, entre na pasta onde você fez o clone desse projeto e rode:

```
pyenv local 3.7.2
```

Depois rode:

```
python -V
```

e você deve ver a versão do python que foi instalada no passo anterior.


# Instalando pipenv

Para instalar o pipenv rode:

```
pip install --user pipenv
```

A partir desse momento você já pode rodar `pipenv` no terminal.

# Instalando o projeto

Entre na pasta do projeto e digite:

```
pipenv install --dev
```

# Rodando os testes

Para rodas os teses, faça:

```
pipenv run test
```

Todos os testes devem passar.


# Definição dos serviços

## Client inicial

Esse é o servico que recebe e parseia a epressão matemática inicial. Então fica sob a responsabilidade dele chamar os outros serviços.


### Endpoints

`POST /eval`

### Entrada

```
{
"expr": "1 + 3 - 3"
}
```

### Saída:

```
{
  "result": 1
}
```


## Soma

### Endpoints

`POST /`

### Entrada

```
{
  "left": 30,
  "right": 40
}
```


### Saída

```
{
  "result": 70
}
```

Esse mesmo mapeamento vale para os serviços: Subtração, Divisão, Multiplicação.


## Potência

### Endpoints

`POST /`

### Entrada

```
{
  "value": 3,
  "power": 2
}
```

### Saída

```
{
  "result": 9
}
```
