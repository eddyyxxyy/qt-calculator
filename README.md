# Simple Calculator

<div style="display: inline-block">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"  alt="Python"/>
  <img src="https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white"  alt="Qt"/>
</div>

> Calculadora simples, grátis e com interface limpa.

Para realização de operações simples de matemática.
Este projeto é para estudo e prática de Python e a biblioteca PySide6.

![estado_atual](docs/versions/v1.0.0.gif)

## Ambiente de Desenvolvimento

> Anteriormente o código estava sendo implementado com PyQT6, porém preferi prosseguir com PySide6. Essa escolha
> se deve à facilidade de utilizar a ferramenta Designer que já vem junto com a biblioteca PySide6 e também pela
> sua licença de uso.

Esta aplicação está sendo desenvolvida com Python 3.10.7 e PySide6 6.3.2 e são, até o presente momento, as únicas
dependências que implicam no real funcionamento da calculadora.
Todas as especificações do projeto se encontram no arquivo pyproject.toml, este projeto está sendo gerenciado com
Poetry e para documentação estou utilizando mkdocs.

Os ícones utilizados: ["Fugue Icons 3.5.6"](https://p.yusukekamiyamane.com/) por
[Yusuke Kamiyamane](https://twitter.com/ykamiyamane) pela licença
[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en)


## Tecnologias

1. [Python 3.10.7](https://www.python.org/downloads/release/python-3107/)
2. [PySide 6.3.2](https://pypi.org/project/PySide6/)


## Features

- Funções aritméticas básicas.
- Dois modos de funcionamento: Padrão e (futuramente) Científico.
- Funções matemáticas mais avançadas: log, ln, abs, etc.


## Métodos de Utilização

No momento em que se encontra essa aplicação, só temos a parte gráfica.

De toda forma, para testar a implementação é necessário estar no diretório
do projeto e executar o seguite comando no cmd/shell:

```
python main.py
```


## Histórico de Atualizações

* 1.0.0
  * Calculadora padrão funcional, como o foco é ter uma interface
  responsiva e bonita, a questão de lidar com os números e outputs
  estão bem simples.
  * Futuramente, posso implementar as outras funções do app, mas o
  que me propus a estudar aqui já foi concluído.
* 0.2.0
  * Criadas as funcionalidades e animação do menu lateral para navegar
  entre as páginas do app.
  * Algumas alterações foram feitas na estrutura do projeto para
  corrigir os erros de run por linha de comando.
  * Foram adicionados icones para os botões do menu lateral.
* 0.1.1
  * Criadas as top e bottom bar, além do content que fica entre elas;
  * Parte gráfica da calculadora padrão implementada na 
    primeira página do aplicativo (em content);
  * Outras páginas serão implementadas no futuro, após real
    implementação dos códigos de cálculos da calculadora padrão,
    entretando, já estão prontas para receber conteúdo gráfico.
* 0.1.0
  * Janela Principal criada com menu lateral.


## Futuro da aplicação

Futuramente, se meus outros projetos não tomarem demais de meu tempo,
irei implementar a calculadora ciêntifica e config. Vou tentar já me
preparar para manter a estrutura do projeto como algo preparado para
receber essa atualização, vinda de mim ou de algum colaborador!


## Meta

Edson Pimenta - [@eeddyyxxyy](https://www.instagram.com/eeddyyxxyy/) - edson.tibo@gmail.com

Distribuído sobre a licença GPL v3. Veja `LICENSE` para mais informações.

[https://github.com/eddyyxxyy](https://github.com/eddyyxxyy)
