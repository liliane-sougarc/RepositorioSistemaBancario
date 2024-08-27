# Desafio: Sistema Bancário em Python

## Descrição do Desafio

Você foi contratado por um grande banco para desenvolver um sistema bancário simples que permita aos usuários realizar operações básicas. Este banco deseja modernizar suas operações e escolheu a linguagem Python para esse projeto. 

Nesta primeira versão, o sistema deve ser capaz de executar três operações principais:

1. **Depósito**: Permitir que o usuário deposite valores na conta bancária.
2. **Saque**: Permitir que o usuário realize saques com limitações específicas.
3. **Extrato**: Mostrar um resumo de todas as transações realizadas e o saldo atual da conta.

## Funcionalidades

- **Depósito**: 
  - O usuário pode depositar valores positivos em sua conta.
  - Todos os depósitos são armazenados e exibidos no extrato.

- **Saque**: 
  - O usuário pode realizar até 3 saques diários, com um limite de R$ 500,00 por saque.
  - O sistema verifica se o usuário tem saldo suficiente antes de realizar o saque.
  - Todos os saques são armazenados e exibidos no extrato.

- **Extrato**: 
  - O extrato lista todos os depósitos e saques realizados na conta.
  - Exibe o saldo atual.
  - Se não houver movimentações, uma mensagem informa que não foram realizadas operações.

## Estrutura do Código

O sistema é implementado em Python e está dividido nas seguintes funções:

- `depositar(valor)`: Realiza um depósito na conta.
- `sacar(valor)`: Realiza um saque, respeitando os limites estabelecidos.
- `exibir_extrato()`: Exibe o extrato das operações realizadas.

### Exemplo de Uso

Aqui está um exemplo de como o sistema pode ser utilizado:

```python
# Exemplo de execução

depositar(1000.00)  # Depósito de R$ 1000,00
sacar(200.00)       # Saque de R$ 200,00
exibir_extrato()    # Exibe o extrato das operações
