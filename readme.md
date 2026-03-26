# 🛡️ DevOps & Security | LogiTech

Este repositório é um ambiente controlado para o estudo de **Ciclo de Vida de Software (SDLC)**, focado em **Integração Contínua (CI)** e **Segurança de Dependências (SCA)**. 

O objetivo é transformar um código instável e vulnerável em uma aplicação protegida por testes automatizados e monitoramento de segurança.

---

## 🗺️ Mapa de Navegação do Laboratório

Acompanhe a evolução do projeto através das branches abaixo. Cada etapa resolve um problema real de engenharia.

| Etapa | Status | Descrição | Atalhos |
| :--- | :---: | :--- | :--- |
| **00. Base** | ⚪ | Código inicial sem validações. | [Ver Código](https://github.com/ceub-integracao-devops/simple-test-ci/commit/230f3a9) |
| **01. CI Fail** | 🔴 | Introdução de Testes e GitHub Actions (Falha). | [Diff Etapa 01](#) |
| **02. CI Pass** | 🟢 | Correção da lógica e aprovação na esteira. | [Diff Etapa 02](#) |
| **03. Security** | ⚠️ | Injeção de vulnerabilidade (Dependabot). | [Diff Etapa 03](#) |
| **04. Final** | ✅ | Projeto consolidado e seguro. | [Diff Etapa 04](#) |

---

## 🚀 Etapa 00: O Estado Inicial (Legacy)

Nesta fase, temos uma classe `Calculadora` que foi entregue sem nenhum teste unitário. 

### 🔍 O que observar:
* **Falta de Governança:** O código pode ser alterado e enviado para a `main` sem qualquer barreira.
* **Risco Oculto:** Existe um erro de lógica na função `operacao_complexa` que passaria despercebido em um deploy manual.
* **Dependências:** O projeto ainda não possui um arquivo de manifesto (`requirements.txt`), dificultando a rastreabilidade de segurança.

### 🛠️ Comandos Úteis (Ambiente Local):
```bash
# Executar a aplicação manualmente
python main.py



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