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
1 + 3 + 5 * (7^2) - 42
```



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
