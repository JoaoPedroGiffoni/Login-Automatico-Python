from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.facebook.com/marketplace/create/item")

navegador.find_element('xpath','//*[@id="email"]').send_keys("Lira")
navegador.find_element('xpath','//*[@id="pass"]').send_keys("pythonimpressionador@gmail.com")

navegador.find_element('xpath', '//*[@id="loginbutton"]').click()