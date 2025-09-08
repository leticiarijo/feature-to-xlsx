# Conversão de Arquivos `.feature` para Excel

Este projeto converte arquivos no formato `.feature` (usados em testes BDD com Gherkin) para arquivos Excel compatíveis com o **Azure Test Plans**. Ele organiza os cenários, passos e resultados esperados em um formato estruturado para facilitar a importação e o gerenciamento de casos de teste.

## 📂 Estrutura do Projeto

- **`ConversaoXlsx.py`**: Script principal que realiza a conversão dos arquivos `.feature` para `.xlsx`.
- **Arquivos `.feature`**: Arquivos de entrada contendo os cenários de teste no formato Gherkin.
- **Arquivos `.xlsx`**: Arquivos gerados pelo script, contendo os cenários estruturados para o Azure Test Plans.

## 🛠️ Funcionalidades

- **Leitura de Arquivos `.feature`**:
  - Identifica cenários, passos (**Dado**, **Quando**, **E**) e resultados esperados (**Então** ou **Entao**).
- **Geração de Arquivos Excel**:
  - Cria um arquivo `.xlsx` para cada arquivo `.feature` processado.
  - Estrutura os dados em colunas compatíveis com o Azure Test Plans:
    - **Work Item Type**
    - **Title**
    - **Test Step**
    - **Step Action**
    - **Step Expected**

## 🖥️ Requisitos

- **Python 3.7+**
- Biblioteca `xlsxwriter`:
  ```bash
  pip install xlsxwriter
  ```

## 🚀 Como Usar

1. **Coloque os Arquivos `.feature` no Diretório do Projeto**:
   - Certifique-se de que os arquivos `.feature` estão no mesmo diretório que o script `ConversaoXlsx.py`.

2. **Execute o Script**:
   - No terminal, navegue até o diretório do projeto e execute:
     ```bash
     python featureToXlsx.py
     ```

3. **Arquivos Gerados**:
   - Para cada arquivo `.feature`, será gerado um arquivo `.xlsx` com o mesmo nome no mesmo diretório.

## 📋 Exemplo de Arquivo `.feature`

```gherkin
Cenário: Login com credenciais válidas
  Dado que o usuário está na página de login
  Quando o usuário insere o nome de usuário e senha corretos
  Então o sistema redireciona para a página inicial
  E exibe uma mensagem de boas-vindas
```

## 🛠️ Estrutura do Código

### Funções Principais

1. **`parse_feature_file(file_path)`**:
   - Lê o arquivo `.feature` e organiza os cenários, passos e resultados esperados.

2. **`write_to_excel(scenarios, output_file)`**:
   - Gera o arquivo Excel com base nos cenários processados.

3. **`process_all_features(directory=".")`**:
   - Processa todos os arquivos `.feature` no diretório especificado.

### Fluxo do Script

1. Lê todos os arquivos `.feature` no diretório.
2. Para cada arquivo:
   - Extrai os cenários e passos.
   - Gera um arquivo `.xlsx` com os dados estruturados.

## ⚠️ Observações

- Certifique-se de que os arquivos `.feature` seguem o formato Gherkin.
- O script suporta tanto **"Então"** quanto **"Entao"** para identificar os resultados esperados.

## 📄 Licença

Este projeto é de uso livre e não possui uma licença específica. Use e modifique conforme necessário.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---
**Autor**: Leticia Rijo
