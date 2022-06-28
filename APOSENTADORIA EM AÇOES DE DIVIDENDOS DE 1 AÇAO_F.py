print(" ")
print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")
ini1=float(input (" Infome seu investimento inicial : "))
print(" ")
print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")

apo1=float(input (" Infome quanto você vai aportar todo mês : "))
print(" ")
print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")
anos=int(input (" Infome quantos anos voçe irá investir : "))
print(" ")
temp19=anos
temp1=anos
temp2=(temp1*12)
print(" ")
print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")
#1
print(" ")
val_acao1=float(input (" Infome quanto vale a ação  : "))
print(" ")

print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")
print(" Não precisa colocar o sinal de porcentagem ( % ), informe apenas com numero")
print(" ")
d_yield1=float(input (" Infome quanto é o Dividend Yield da ação  : "))
print(" ")
print(" Por favor informe o numero decimal com ponto ( . ), não com ( , )")
print(" ")
dividendo1=float(input (" Infome quanto é o Dividendo distribuido ultimamente pela ação  : "))
print(" ")
print(" ")
prco_teto_med1=float(dividendo1/0.06)
prco_teto_med1=round(prco_teto_med1,2)
print(" O preço teto médio da ação  é de  R$",prco_teto_med1,"Reais")
print(" ")
print(" ")
#1

#2
quant1=float(ini1/val_acao1)
quant1=round(quant1,2)
quant2=float(apo1/val_acao1)
quant2=round(quant2,2)
print ("COM O VALOR DO APORTE INICIAL DE R$ ",ini1,"REAIS VOCE COMPRARÁ APROXIMADAMENTE ",quant1,"AÇÕES")
print ("COM O VALOR DO APORTE MENSAL  DE R$ ",apo1,"REAIS VOCE COMPRARÁ APROXIMADAMENTE ",quant2,"AÇÕES")
d_yield_médio=(d_yield1)
d_yield_médio=round(d_yield_médio,2)
print(" O Dividendo medio do conjunto das ações do investimento é de ",d_yield_médio,"% .")

print(" ")


soma_val_acao=(val_acao1)
val_acao=soma_val_acao
val_acao=round(val_acao,2)
soma_dividendo=(dividendo1)
dividendo=soma_dividendo
dividendo=round(dividendo,2)
print(" Você precisará de R$ ",val_acao,"Reais para cada  ação ")
print(" ")
print(" Você terá direito a R$ ",soma_dividendo," Reais em dividendos ao ano por cada ação" )
print("")
val1=((ini1*dividendo)/val_acao)
val2=((apo1*dividendo)/val_acao)
init1=round(ini1,2)
val1=round(val1,0)
apo1=round(apo1,2)
val2=round(val2,0)
print(" Por seu  aporte inicial de R$ ",ini1,"Reais em bloco de açoes ")
print(" ")
print(" Você terá direito a R$ ",val1," Reais em dividendos ao ano por seu aporte inicial de R$" ,ini1,"Reais")
print(" ")

print(" Para cada aporte de R$ ",apo1,"Reais para cada bloco de açoes")
print(" ")
print(" Você terá direito a R$ ",val2," Reais em dividendos ao ano por cada aporte de R$" ,apo1,"Reais")
print(" ")
dividendo1=val1
dividendo2=val2

for c in range(0,temp1):
    ini2=float(((dividendo1*dividendo1)/ini1))
    round(ini2,2)
    ini3=(ini1+ini2)
    round(ini3,2)
    ini3=ini3+val1
    round(ini3,2)
print("")


for c in range(0,temp2):
    apo2=float(((dividendo2*dividendo2)/apo1))
    round(apo2,2)
    apo3=(apo1+apo2)
    round(apo3,2)
    apo3=apo3+val2
    round(apo3,2)
print("")


ini4=ini3
apo4=apo3
val1=val1*temp1
val2=val2*temp2

val3=(ini4+apo4+val1+val2)
round(val3,2)
quant3=(val3/val_acao1)
quant3=round(quant3,0)
print ("")
print ("VOCE TERÁ NO FINAL DE ",temp19,"ANOS COMPRADO UM TOTAL DE ",quant3," AÇÕES")
print ("")
aposentadoria1=val3
aposentadoria1=round(aposentadoria1,2)
aposentadoria2=(val3/12)
aposentadoria2=round(aposentadoria2,2)
aposentadoria3=(val3/22)
aposentadoria3=round(aposentadoria3,2)
aposentadoria4=(val3/23)
aposentadoria4=round(aposentadoria4,2)
aposentadoria5=(val3/30)
aposentadoria5=round(aposentadoria5,2)
print ("E RECEBERRÁ EM DIVIDENDOS : R$ ",aposentadoria1, "Reais TODO ANO")
print ("")

print(" ")
print(" Sua aposentadoria anual é de              R$ ",aposentadoria1, "Reais")
print(" ")
print(" Sua aposentadoria mensal em 12 meses é de R$ ",aposentadoria2, "Reais")
print(" ")
print(" Sua aposentadoria mensal em 22 meses é de R$ ",aposentadoria3, "Reais")
print(" ")
print(" Sua aposentadoria mensal em 23 meses é de R$ ",aposentadoria4, "Reais")
print(" ")
print(" Sua aposentadoria mensal em 30 meses é de R$ ",aposentadoria5, "Reais")
print(" ")

print(" Pressione uma tecla para fechar ")

input(" ")
