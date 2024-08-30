# Sistema de Operações Bancárias

Este projeto é uma simulação simples de um sistema bancário, implementado em Python. Ele permite ao usuário realizar três operações principais: **depósito**, **saque** e **extrato**. O objetivo é proporcionar uma experiência básica de operações bancárias, onde o saldo é atualizado conforme as transações são realizadas.

Importante resaltar que esse projeto considera um único usuário, assim não é necessário fazer a verificação de numeros de conta e agencia, por exemplo.

## Funcionalidades

- **Saque:** Permite ao usuário sacar um valor do saldo, desde que haja fundos suficientes, o valorque o usuário deseja sacar seja um número possitivo, não ultrapasse R$500,00 por saque e não atinga o limite máximo de 3 saques por operação.

- **Depósito:** Permite ao usuário depositar um valor (positivo), que será adicionado ao saldo.

- **Extrato:** Exibe o histórico de movimentação da conta e saldo atual da conta.

## Como Usar

1. **Inicialização:**
   - Ao iniciar o programa, o usuário é saudado com um menu de opções.

2. **Menu de Operações:**
   - `1 - SACAR`: Solicita ao usuário o valor a ser sacado e, se houver saldo suficiente, deduz o valor do saldo atual.
   - `2 - DEPOSITAR`: Solicita ao usuário o valor a ser depositado e adiciona-o ao saldo atual.
   - `3 - EXTRATO`: Exibe o histórico de movimentação da conta e saldo atual da conta.
   - `0 - SAIR`: Encerra o programa.

3. **Interação:**
   - O usuário deve escolher a operação desejada digitando o número correspondente.
   - O sistema continuará a operar até que o usuário escolha a opção `0` para sair.


## Requisitos

- Python 3.x instalado.

## Execução

Para executar o sistema, basta rodar o script Python. O menu será exibido, e você poderá interagir com ele conforme as instruções.

---