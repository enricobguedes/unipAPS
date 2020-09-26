from tkinter import *
from cryptography.fernet import Fernet, MultiFernet

##DECLARAÇÃO DE VARIÁVEIS PARA OBTENÇÃO DE UMA CHAVE##
encryptKey = Fernet(Fernet.generate_key())
decryptKey = Fernet(Fernet.generate_key())
eC = MultiFernet([encryptKey, decryptKey])
eD = MultiFernet([decryptKey, encryptKey])

#INÍCIO DO PROGRAMA##
class Application:
    def __init__(self, master=None):

    	#DECLARAÇÃO + CONFIGURAÇÃO DE LAYOUT/CAIXAS DE TEXTO NO PROGRAMA##
    	self.introTextoLbl = Label(master,text="Aqui está nosso programinha!", width=100, height=5)		## TÍTULO

    	self.entradaDadosLbl = Label(master,text="Encriptografar: ")	##NOME ANTERIOR A BARRA DE ENTRADA DE DADOS

    	self.fraseEntradaStr = Entry(master, width=100, bg='white', textvariable="")	##BARRA DE ENTRADA DE DADOS

    	self.fraseEntradaLbl = Label(master, width=100, bg='white', text="Chave para encriptografar")	#LOCAL PLACE HOLDER PARA GERAR A CHAVE DE ENCRIPTOGRAFIA

    	self.botaoEncriptografar = Button(master, width=10, text="Criptografar", command= self.Encriptografar) #BOTÃO MAIS À ESQUERDA PARA EXECUTAR FUNÇÃO DE CRIPTOGRAFAR

    	self.botaoDecriptografar = Button(master, width=10, text="Decriptografar", command= self.Descriptografar) #BOTÃO MAIS À DIREITA PARA EXECUTAR FUNÇÃO DE DESCRIPTOGRAFAR

    	self.fraseSaida1Lbl = Label(master, width=100, bg='white', text="Chave para descriptografar") #PLACE HOLDER PARA MOSTRAR QUAL CHAVE FOI USADA PARA DESCRIPTOGRAFAR

    	self.fraseSaida2Lbl = Label(master, width=100, bg='white', text="Mensagem original")	#MENSAGEM QUE FORA CRIPTOGRAFADA ORIGINALMENTE

    	#FECHANDO CONFIGURAÇÕES + POSICIONAMENTO DO LAYOUT/CAIXAS DE TEXTO##
    	##STICKY SIGNIFICA POSICIONAMENTO FIXO, SEGUE O PRINCIPIO DA ROSA DOS VENTOS: NORTE, SUL, LESTE E OESTE (NORTH, SOUTH, EAST E WEST, RESPECTIVAMENTE)##

    	self.introTextoLbl.grid(column=0,row=0) #TITULO

    	self.entradaDadosLbl.grid(column=0,row=1, sticky= W) #LABEL DA BARRA DE DADOS

    	self.fraseEntradaStr.grid(column=0,row=1, sticky= E) #BARRA DE ENTRADA DE DADOS

    	self.fraseEntradaLbl.grid(column=0,row=2) #LOCAL PARA GERAR KEY ENCRIPT.

    	self.botaoEncriptografar.grid(row=3, sticky=W) #BOTAO FUNÇÃO ENCRIPT

    	self.botaoDecriptografar.grid(row=3,sticky=E) #BOTAO FUNCAO DECRIPT

    	self.fraseSaida1Lbl.grid(row=4) #CHAVE DE DECRYPT
    	
    	self.fraseSaida2Lbl.grid(row=5) # MENSAGEM ORIGINAL

    def Encriptografar(self):
    	#função para encriptografar
    	errado = "Tente novamente." #tentativa para aparecer na Label de keys
    	encriptografar = self.fraseEntradaStr.get() #Busca e atríbui texto digítado na variável.
    	global textoEncod #declaração global para ser usada na próx função

    	#tentativa falha de fazer funcionar a variavel "errado"
    	for x in encriptografar:
    		if x != "" or None or 0:
    			encriptografar = encriptografar.encode() #transforma a string em bytes
    			textoEncod = eC.encrypt(encriptografar) #encodifica os bytes
    			self.fraseEntradaLbl["text"] = textoEncod #frase exposta no label de chave
    			break 
    		else: ###não consigo fazer aparecer uma mensagem quando o usuário não escreve nada na barra###
    			self.fraseEntradaLbl["text"] = errado
    			break


    def Descriptografar(self):
    	#função para descriptografar
    	self.fraseSaida1Lbl["text"] = textoEncod #frase exposta no label de chave de descript.
    	textoDescr = eD.decrypt(textoEncod) #descriptografando dados para bytes
    	textoLimpo = textoDescr.decode() # transformando bytes em string
    	self.fraseSaida2Lbl["text"] = textoLimpo #mensagem original


root = Tk()
Application(root)
root.mainloop()
