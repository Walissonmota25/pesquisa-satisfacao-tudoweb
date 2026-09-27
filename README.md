# 📊 Pesquisa de Satisfação — TudoWeb

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</p>

<p align="center">
  🗣️ <strong>Ouvir o cliente é o primeiro passo para melhorar o atendimento.</strong>
</p>

---

## 💡 Sobre o projeto

Este projeto foi desenvolvido para a empresa fictícia **TudoWeb** com o objetivo de realizar uma pesquisa de satisfação com seus clientes.

O programa coleta informações de **50 entrevistados**, como:

- 👤 Nome
- 🎂 Idade
- ⭐ Opinião sobre o atendimento

Depois de coletar as respostas, o sistema contabiliza a quantidade de avaliações **EXCELENTE** e **RUIM**.

---

## 🎯 Objetivo

O principal objetivo é colocar em prática conceitos de **programação estruturada**, utilizando:

```text
🔁 Estrutura de repetição
🔀 Estruturas de decisão
📦 Variáveis
➕ Contadores
⌨️ Entrada de dados
🖥️ Saída de informações
```

---

## 🧠 Como funciona?

O sistema apresenta três opções de avaliação:

| Opção | Avaliação |
|:---:|---|
| 1️⃣ | ⭐ EXCELENTE |
| 2️⃣ | 👍 BOM |
| 3️⃣ | 👎 RUIM |

Durante a pesquisa, o programa verifica a opção escolhida utilizando estruturas de decisão.

### 🔄 Fluxo do programa

```text
        👤 Entrevistado
              │
              ▼
       📝 Nome e idade
              │
              ▼
       💬 Opinião sobre
        o atendimento
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     ⭐ 1    👍 2    👎 3
  EXCELENTE   BOM     RUIM
       │              │
       ▼              ▼
   +1 excelente    +1 ruim
       │              │
       └──────┬───────┘
              ▼
       🔁 Próximo entrevistado
              │
              ▼
       📊 Resultado final
```

---

## 🐍 Tecnologias utilizadas

### Python

Linguagem utilizada para desenvolver toda a lógica do sistema.

### GitHub

Utilizado para armazenar e compartilhar o projeto.

### Visual Studio Code

Ambiente utilizado para escrever e executar o programa.

---

## ⚙️ Estrutura do código

O programa utiliza um `for` para repetir a pesquisa:

```python
for i in range(quantidade_entrevistados):
```

As respostas são verificadas através de:

```python
if
elif
else
```

E os resultados são contabilizados através de variáveis:

```python
excelente = 0
ruim = 0
```

Quando uma resposta corresponde à classificação, o contador é atualizado.

---

## 🧪 Teste do programa

Para validar o funcionamento, foi realizado um teste com **10 entrevistados**.

O teste verifica se:

- ✅ Os dados são solicitados corretamente;
- ✅ A estrutura `for` realiza as repetições;
- ✅ As opiniões são classificadas;
- ✅ As respostas EXCELENTE são contabilizadas;
- ✅ As respostas RUIM são contabilizadas;
- ✅ O resultado final é exibido corretamente.

---

## 📸 Evidências

Os prints dos testes estão disponíveis na pasta:

```text
📁 prints
  🖼️ codigo1.png
  🖼️ codigo2.png
  🖼️ execucao.png
```

O primeiro  e segundo mostra o código desenvolvido e o terceiro apresenta o programa sendo executado no terminal.

---

## ▶️ Como executar

### 1. Tenha o Python instalado

Confira a instalação com:

```bash
python --version
```

### 2. Abra a pasta do projeto

Entre na pasta:

```text
pesquisa-tudoweb
```

### 3. Execute o programa

No terminal, utilize:

```bash
python app.py
```

### 4. Responda à pesquisa

Informe os dados solicitados pelo sistema.

---

## 📈 Resultado

Ao finalizar as entrevistas, o programa apresenta:

```text
======================================
          RESULTADO DA PESQUISA
======================================

Quantidade de respostas EXCELENTE: XX
Quantidade de respostas RUIM: XX
```

Dessa forma, é possível visualizar rapidamente a quantidade de avaliações positivas e negativas recebidas durante a pesquisa.

---

## 🌱 Aprendizado

Este projeto ajudou a praticar o uso de **estruturas de repetição e decisão em Python**, além de trabalhar com entrada de dados, contadores e organização de um projeto utilizando GitHub.

> 💭 **Programar também é transformar uma necessidade em uma sequência de decisões que o computador consegue entender.**

---

## 👨‍💻 Autor

**Walisson Da Silva Mota**

🎓 Projeto acadêmico — Desenvolvimento de Sistemas

💻 Python • GitHub • Visual Studio Code

---

<p align="center">
  ⭐ Projeto desenvolvido para fins acadêmicos ⭐
</p>