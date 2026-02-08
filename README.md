# Fuel Control - User Guide

This document explains how to install the `fuel_control` module, set access rights, and use the main features.

## 0) Ambientation:
Windows WSL installation (if you use a Linux distribution, ignore this part):
1. Open PowerShell as an administrator.
2. Run: wsl --install.
3. Restart your computer when prompted.
4. Open Ubuntu (or the installed distro) and create a username and password.
5. Update the system with sudo apt update && sudo apt upgrade.
8. Install Docker Desktop or Docker directly in the Linux terminal.
   (See Docker documentation [hub](https://docs.docker.com/get-started/get-docker/))

**Installation**
1. In WSL/Linux, choose a working folder. E.g.: ~/projects.
2. Create the folder: mkdir -p ~/projects and enter it: cd ~/projects.
3. Create a folder for the challenge, for example: mkdir -p odoo19_setup.
4. Enter it: cd odoo19_setup.
5. Clone the installation script (Yenthe666):
git clone https://github.com/Yenthe666/InstallScript.git
6. Enter the script folder: cd InstallScript.
7. Check the version 19 script (when available, use the appropriate .sh).
8. Give execution permission: chmod +x odoo_install.sh (or the version 19 script).
9. Run the script according to the repo documentation.
10. Clone this repository
11. Alternative: if you prefer Docker, create a docker-compose.yml for testing in the project folder and upload Odoo with the command docker compose up -d.
12. In Docker, open the browser and finish creating the database at localhost:8069.
13. Create your project structure in a separate folder, e.g., ~/projects/erp_odoo_19_challenge.
14. Update the list of Apps and install the module by searching for “Fuel Control.”

## 1) Module installation

1. Ensure the `custom_addons/` directory is included in the Odoo `addons_path`.
2. Copy the `fuel_control` module into `custom_addons/`.
3. Restart the Odoo service.
4. In Odoo, open **Apps**.
5. Click **Update Apps List**.
6. Search for **Fuel Control** and click **Install** (or **Upgrade** if already installed).

> Note: the module depends on `fleet`, `purchase`, and `stock`.

## 2) Assign access to users

The module creates three groups:
- **Fuel Control - Driver**: registers refuels without manual stock changes.
- **Fuel Control - Analyst**: views reports.
- **Fuel Control - Administrator**: full access (includes stock entries and settings).

Steps:
1. Open **Settings > Users & Companies > Users**.
2. Select the desired user.
3. In the permissions tab, assign one of the groups above.
4. Save.
5. Refresh the page.

> Note: the menu will not appear for users without the proper group.

## 3) How to use the module

### 3.1 Refuels
1. Go to **Fuel Control > Refuels**.
2. Click **Create**.
3. Fill in:
   - vehicle / Plate
   - Date and Time
   - Odometer / Hour Meter (if applicable)
   - Liters
   - Price per Liter
4. The total is calculated automatically.
5. Save.

> Tank stock is reduced automatically when a refuel is saved.

### 3.2 Manual stock entry
1. Go to **Fuel Control > Stock Entries** (admin only).
2. Click **Create**.
3. Fill in tank, date, liters, and price.
4. Save.

> Tank stock is increased automatically.

### 3.3 Stock entry from purchase receipt
1. Go to **Inventory > Receipts**.
2. Open an incoming receipt.
3. In the **Fuel** tab:
   - Fuel Tank
   - Fuel Liters
   - Price per Liter
4. Click **Validate**.

> The module automatically generates a stock entry linked to the receipt.

### 3.4 Reports
1. Go to **Fuel Control > Reports**.
2. Open **Refuels** or **Entries**.
3. Use Pivot/Graph for analysis.

## 4) Rules and notes

- Tank capacity is fixed at 6000 L.
- Stock cannot be negative or exceed capacity.
- Initial tank data loads only on first install (`noupdate`).

## 5) Troubleshooting

- **Menu not visible**: confirm the user group and update the Apps list.
- **Stock resets to 6000**: ensure the module was upgraded after the `noupdate` data change.
- **Permission error**: verify the assigned group.

## 6) Translations

- The module is implemented in English and can be translated to other languages following standard Odoo practices.

- **Brazilian Portuguese**:
# Fuel Control - Guia de Uso

Este documento explica como instalar o modulo `fuel_control`, configurar acessos e utilizar as principais funcionalidades.

## 0) Ambientation:
Windows WSL instalation ( if you uses linux distribuition, ignore this part:
1. Open PowerShell as an administrator.
2. Run: wsl --install.
3. Restart your computer when prompted.
4. Open Ubuntu (or the installed distro) and create a username and password.
5. Update the system with sudo apt update && sudo apt upgrade.
8. instale o DOcker Desktop ou o docker diretamente no terminal linux.
   (consultar documentação Docker [hub](https://docs.docker.com/get-started/get-docker/))

**instalação do ambiente**
1. No WSL/Linux, escolha uma pasta de trabalho. Ex.: ~/projects.
2. Crie a pasta: mkdir -p ~/projects e entre nela: cd ~/projects.
3. Crie uma pasta para o desafio, por exemplo: mkdir -p odoo19_setup.
4. Entre nela: cd odoo19_setup.
5. Faça o clone do script de instalacao (Yenthe666):
git clone https://github.com/Yenthe666/InstallScript.git
6. Entre na pasta do script: cd InstallScript.
7. Verifique o script da versao 19 (quando houver, use o .sh adequado).
8. Dê permissao de execucao: chmod +x odoo_install.sh (ou o script da versao 19).
9. Execute o script conforme a documentacao do repo.
10. Clone esse repositório
11. Alternativa: se preferir Docker, criei um docker-compose.yml para testes na pasta do projeto e suba o Odoo com o comando docker compose up -d.
12. Em Docker, abra o navegador e finalize a criacao do banco no localhost:8069.
13. Crie a estrutura do seu projeto em uma pasta separada, ex.: ~/projects/desafio_erp_odoo_19.
14. Atualize a lista de Apps e instale o modulo buscando por "Fuel Control".


## 1) Instalacao do modulo

1. Garanta que o diretorio `custom_addons/` esteja configurado no `addons_path` do Odoo.
2. Copie o modulo `fuel_control` para `custom_addons/`.
3. Reinicie o servico do Odoo.
4. No Odoo, abra **Apps**.
5. Clique em **Update Apps List**.
6. Procure por **Fuel Control** e clique em **Install** (ou **Upgrade**, se ja estiver instalado).

> Observacao: o modulo depende de `fleet`, `purchase` e `stock`.

## 2) Atribuir acesso aos usuarios

O modulo cria tres grupos:
- **Fuel Control - Driver**: registra abastecimentos, sem alterar estoque manualmente.
- **Fuel Control - Analyst**: visualiza relatorios.
- **Fuel Control - Administrator**: acesso total (inclui entradas de estoque e configuracoes).

Passos:
1. Abra **Settings > Users & Companies > Users**.
2. Selecione o usuario desejado.
3. Na aba de permissoes, atribua um dos grupos acima.
4. Salve.
5. Atualize a Página. 
Alternativo: 
1. Abra **Settings > Users & Companies > Groups**.
2. Procure pelo grupo desejado e entre no grupo
3. Selecione o usuario desejado.
4. Na aba de permissoes, atribua um dos grupos acima.
5. Salve.
6. Atualize a Página. 

- notas: 
1. O módulo não aparecerá como ítens de menú para usuarios sem permição.
2. Caso esteja em um ambiente com Portugues BR, é possivel que o nome do grupo esteja traduzido, sendo assim, busque por **Combustivél** ou **Controle de Combustivél**


## 3) Como utilizar o modulo

### 3.1 Abastecimentos (Refuels)
1. Menu **Fuel Control > Refuels**.
2. Clique em **Create**.
3. Preencha:
   - vehicle / Plate
   - Date and Time
   - Odometer / Hour Meter (se aplicavel)
   - Liters
   - Price per Liter
4. O total e calculado automaticamente.
5. Salve.

> O estoque do tanque e reduzido automaticamente ao salvar o abastecimento.

### 3.2 Entrada manual de estoque
1. Menu **Fuel Control > Stock Entries** (somente admin).
2. Clique em **Create**.
3. Preencha o tanque, data, litros e preco.
4. Salve.

> O estoque do tanque e aumentado automaticamente.

### 3.3 Entrada via recebimento de compra
1. Menu **Inventory > Receipts**.
2. Abra um recebimento de entrada.
3. Aba **Fuel**:
   - Fuel Tank
   - Fuel Liters
   - Price per Liter
4. Clique em **Validate**.

> O modulo gera automaticamente uma entrada de estoque vinculada ao recebimento.

### 3.4 Relatorios
1. Menu **Fuel Control > Reports**.
2. Acesse **Refuels** ou **Entries**.
3. Use Pivot/Graph para analise.

## 4) Regras e observacoes

- A capacidade do tanque e fixa em 6000 L.
- O estoque nao pode ficar negativo nem exceder a capacidade.
- Os dados iniciais do tanque sao carregados apenas na primeira instalacao (`noupdate`).

## 5) Solucao de problemas

- **Menu nao aparece**: confirme o grupo do usuario e atualize a lista de Apps.
- **Estoque volta a 6000**: verifique se o modulo foi atualizado apos o `noupdate` no XML de dados.
- **Erro de permissao**: verifique o grupo atribuido ao usuario.

## 6) Traduções

- O módulo foi desenvolvido em ingles e traduzidos para o idioma Português como mandam os padroes de desenvolvimento python

