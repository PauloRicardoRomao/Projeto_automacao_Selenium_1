from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#Buscar site
navegador.get('https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=5685072762092990139&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1032092&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1')

#Localizar campo de busca de produtos
busca_item = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("xpath", '//*[@id="twotabsearchtextbox"]')))

#Realizar busca
busca_item.send_keys('Iphone')
busca_item.send_keys(Keys.ENTER)

#Localizar filtro de preço
filtro_preco_min = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("xpath", '//*[@id="low-price"]')))
filtro_preco_max = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("xpath", '//*[@id="high-price"]')))

#Realizar filtragem de preço

preco_min = 1500
preco_max = 4000
if preco_min > 0:
    filtro_preco_min.send_keys(preco_min)
if preco_max > 0:
    filtro_preco_max.send_keys(preco_max)

botao_ir = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("xpath", '//*[@id="a-autoid-3"]/span/input')))
botao_ir.send_keys(Keys.RETURN)




#Opção para fechar a automação
input("Pressione Enter para sair...")

