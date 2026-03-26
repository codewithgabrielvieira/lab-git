# 🛡️ DevOps | LogiTech

Este repositório é um ambiente controlado para o estudo de **Ciclo de Vida de Software (SDLC)**, focado em **Integração Contínua (CI)**. 

O objetivo é transformar um código instável e vulnerável em uma aplicação protegida por testes automatizados.

---

## 🗺️ Mapa de Navegação do Laboratório

Acompanhe a evolução do projeto através das branches abaixo. Cada etapa resolve um problema real de engenharia.

| Etapa | Status | Descrição | Código / Diff | Actions |
| :--- | :---: | :--- | :--- | :--- |
| **00. Base** | ⚪ | Código inicial sem validações. | [Ver Commit](https://github.com/ceub-integracao-devops/simple-test-ci/commit/230f3a9) | N/A |
| **01. CI Fail** | 🔴 | Introdução de Testes e GitHub Actions (Falha). | [Diff Etapa 01](https://github.com/ceub-integracao-devops/simple-test-ci/compare/main...01-falha-logica) | [Logs Falha](https://github.com/ceub-integracao-devops/simple-test-ci/actions/runs/23573210411/job/68640114167) |
| **02. CI Pass** | 🟢 | Correção da lógica e aprovação na esteira. | [Diff Etapa 02](https://github.com/ceub-integracao-devops/simple-test-ci/pull/2/changes/4f84957cab4263415067e3aece85f9049b989437) | [Actions Etapa 02](https://github.com/ceub-integracao-devops/simple-test-ci/actions/runs/23574307704/job/68643379417) |

---

## 🚀 Etapa 00: O Estado Inicial (Legacy)

Nesta fase, temos uma classe `Calculadora` que foi entregue sem nenhum teste unitário. 

### 🔍 O que observar:
* **Falta de Governança:** O código pode ser alterado e enviado para a `main` sem qualquer barreira.
* **Risco Oculto:** Existe um erro de lógica na função `operacao_complexa` que passaria despercebido em um deploy manual.
* **Dependências:** O projeto ainda não possui um arquivo de manifesto (`requirements.txt`), dificultando a rastreabilidade de segurança.

---

## 🔴 Etapa 01: A Denúncia do Erro (CI Fail)

Nesta etapa, introduzimos a **Governança Automatizada**. O objetivo é demonstrar como um teste unitário bem escrito impede que um erro de lógica chegue ao usuário final.

### 🛠️ O que foi adicionado:
* **`test_main.py`**: Contém asserções que validam a regra de negócio (multiplicação).
* **`.github/workflows/ci.yml`**: Define a esteira de CI que instala o Python e executa o motor de testes.

### 📉 O que observar no GitHub:
1. Vá na aba **Actions** do repositório.
2. Você verá um workflow falhando (ícone X vermelho).
3. Ao clicar no erro, você verá a mensagem: `AssertionError: assert 7 == 10`.

**Status Atual:** O código está bloqueado para merge pois não atende aos requisitos de qualidade.

---
[Ver código do Teste](https://github.com/ceub-integracao-devops/simple-test-ci/blob/01-falha-logica/test_main.py) | [Ver Logs do Erro no Actions](https://github.com/ceub-integracao-devops/simple-test-ci/actions)


## 🟢 Etapa 02: A Cura (CI Pass)

Nesta etapa, corrigimos o erro de lógica identificado pelos testes. Ao realizar o push, a esteira de CI validará automaticamente se a mudança surtiu efeito.

### 🛠️ O que mudou:
* **`main.py`**: O operador `+` foi substituído por `*`.
* **Resultado:** O GitHub Actions agora deve exibir um "Check" verde.

### 📈 O que observar:
1. O Pull Request da branch `02-ci-corrigido` mostrará que todos os testes passaram.
2. Este é o momento em que o **Tech Lead** (ou o robô) autoriza o merge para a produção.

---
[Ver Diff da Correção](https://github.com/ceub-integracao-devops/simple-test-ci/compare/01-falha-logica...02-ci-corrigido) | [Ver CI com Sucesso](https://github.com/ceub-integracao-devops/simple-test-ci/actions)
