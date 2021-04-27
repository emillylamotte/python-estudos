import pyautogui #automação do mouse e teclado
import time #controla tempo de execução do programa
import pyperclip #permite copiar e colar com python

pyautogui.PAUSE = 1 #sempre que executar um comando esperar 1s, para aguardar o carregamento das páginas
pyautogui.alert("O processo vai começar, dê ok e aguarde a execução")

##Passo 1: Entrar no sistema de dados

pyautogui.hotkey ("ctrl","v") #abre uma nova aba no navegador
link = "endereço" #glink de acesso ao sistema
pyperclip.copy (link) #copia o link e cola no navegador
pyautogui.hotkey ("ctrl","v")
pyautogui.press("enter")
time.sleep(5) #pausa 5s a execução pra página carregar

##Passo 2: Entrar na pasta do sistema que contém os dados

pyautogui.click(935, 669, clicks=2)#local onde deve ocorrer o click (x,y, nº de clicks)

##Passo 3: Baixar arquivo de dados

pyautogui.click(2027,911)
pyautogui.click(3327, 392)
pyautogui.click(2794, 1487)
time.sleep(10)

##Passo 4: Analisar os dados

import pandas as pd #pd será o atalho

tabela = pd.read_excel(r "endereço-arquivo", sheet_name=1) #armazena o arquivo na variavel, retirando da aba 1 da planilha
display(tabela) #mostra a tabela na tela
faturamento = tabela["Valor Final"].sum() #coluna "valor final" da tabela; sum: soma todos os elementos da coluna
qtd_produtos = tabela["Quantidade"].sum()

##Passo 5: Entrar no email

pyautogui.hotkey ("ctrl","v") #abre uma nova aba no navegador
link = "link-acesso-email" #guarda o link de acesso ao email
pyperclip.copy (link)#copia o link e cola no navegador
pyautogui.hotkey ("ctrl","v")
pyautogui.press("enter")
time.sleep(8)#pausa 8s pra página carregar

##Passo 6: Criar email
pyautogui.click(2027,911) #botao escrever
time.sleep(3)
pyautogui.write("email-destino") #endereço do destinatário
pyautogui.press("tab")#escolhe o destino
pyautogui.press("tab")#vai para o assunto
assunto = "Relatório dos dados analisados"
pyperclip.copy(assunto) 
pyautogui.hotkey("ctrl", "v") #adiciona o assunto

##Passo 7: Preencher o email
pyautogui.press("tab")#vai para o corpo do email
texto_email = f""" 
Bom dia, segue os dados analizados durante esta manhã:

O faturamento foi de: R${faturamento:,.2f}.
A quantidade de produtos vendidos foi: {qtd_produtos} produtos. 

Att, Analista.

"""
#f indica que tem texto dinâmico, ,.2f determina 2 casas decimais para esse valor
pyperclip.copy(texto_email)
pyautogui.hotkey("ctrl","v")#adiciona o corpo do email

##Passo 8: Enviar o email
pyautogui.hotkey("ctrl", "enter")#envia o relatório

##Fim
pyautogui.alert("Fim do processo, confira o email de destino.")
