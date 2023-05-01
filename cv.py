import  requests

fund = [
"""\33[41m""" ,
"""\33[42m""" ,
"""\33[43m""" ,
"""\33[44m """,
"""\33[45m""" ,
"""\33[46m """,
"""\33[47m""" 
]
fund0 ="\33[40m"

cor = [

"""\33[1,32m"""

]
cor0 = [

"""\33[1,30m"""
]

class conversor():
    
    # MENU DE OPÇÕES

    def __init__(self):
    
       self.menu = input(f"\n\n{fund[1]}CONVERSOR DE MOEDA {fund0}💰💰\n\n \n[1]USD\n[2]EUR\n[3]BTC\n\nOPCÃO-> ")
       
    	
       if self.menu =="1":
           self.menu ="USD"
       elif self.menu =="2":
           self.menu="EUR"
       elif self.menu =="3":
           self.menu="BTC"
       else :
           cor[0]
           print(f"{fund[2]} ⚠️ Digite uma das opção ⚠️{fund0}")
       try:
               
           self.rq = requests.get(f"https://economia.awesomeapi.com.br/json/last/{self.menu}-BRL")
       
           self.moeda = self.rq.json()
       except:
           
           print("Sem conexão a rede")

    def selec_moeda(self):
        
        self.dado = float(self.moeda[self.menu+"BRL"]["high"])
        self.valor = float(input(f"\n\nValor em {self.menu}| "))
       
        if self.menu =="USD":
            self.menu = "Dolar"
            
        elif self.menu =="EUR":
            self.menu = "Euro"
        
        elif self.menu =="BTC":
            self.menu ="Bitcoin"

    def calculo(self):
        
        resultado = self.valor * self.dado

        
        print("\n\n {} {} é igual a R${:.2f} Reais\n\n".format(self.valor, self.menu,resultado))

while True:
    
    inicio = conversor()
    inicio.selec_moeda()
    inicio.calculo()
    
    opc = input("Deseja voltar? [y/n]\n-> ")
    
    if opc == "n":
        break
