# Automação de login com Selenium

Este repositório contém um script em Python que automatiza o processo de login usando Selenium e ChromeDriver.

## Pré-requisitos
- Python
- Biblioteca Selenium
- Navegador Chrome

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/seu-nome-de-usuario/seu-repositorio.git
   ```

2. Instale as dependências necessárias usando o pip:

   ```
   pip install selenium webdriver_manager
   ```

3. Baixe o executável do ChromeDriver compatível com a versão do seu navegador Chrome. Você pode baixá-lo no site oficial do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), ou pode usar o pacote `webdriver_manager` para instalar automaticamente o ChromeDriver compatível:

   ```python
   from selenium import webdriver
   from webdriver_manager.chrome import ChromeDriverManager

   driver = webdriver.Chrome(ChromeDriverManager().install())
   ```

## Uso

1. Abra o script Python no seu editor preferido.

2. Substitua os valores fictícios nas linhas a seguir com suas credenciais de login do Facebook:

   ```python
   navegador.find_element('xpath','//*[@id="email"]').send_keys("SEU_EMAIL_AQUI")
   navegador.find_element('xpath','//*[@id="pass"]').send_keys("SUA SENHA AQUI")
   ```

3. Salve as alterações no script.

4. Execute o script usando o Python:

   ```
   python nome_do_script.py
   ```

   O script abrirá um navegador Chrome e automaticamente navegará até a página de login do Facebook Marketplace, inserirá suas credenciais de login e clicará no botão de login.

5. Personalize o script de acordo com suas necessidades. Você pode modificar as expressões XPath ou adicionar ações adicionais para interagir com o Facebook Marketplace.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou desejar adicionar novos recursos, abra uma issue ou envie um pull request.

## Agradecimentos

- [Selenium](https://www.selenium.dev/) - Framework de automação de navegador
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) - WebDriver para o navegador Chrome
- [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) - Gerenciador de WebDriver para Python
