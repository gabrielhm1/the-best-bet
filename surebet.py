oddMandante = 3  #pegar da pagina
oddVisitante = 2.5
oddEmpate = 5.2

indiceOdds = [1/oddMandante,1/oddVisitante,1/oddEmpate]

somaIndice = 0.0

ApostaInicial = 100 #inserido pelo usuario

valorLucro = 0.0
porcentLucro = 0.0

for i in range(3):
    somaIndice = somaIndice + indiceOdds[i]

if(somaIndice < 1.0):
    print("há uma surebet")

    porcentApostas = [] #porcentagem que deverá ser apostada em cada odd para garantir surebet
    for j in range(3):
        porcentApostas.append(indiceOdds[j]/somaIndice)
    
    valoresApostas = []
    for k in range(3):
        valoresApostas.append(porcentApostas[k]*ApostaInicial)

    valorLucro = round((valoresApostas[0]*oddMandante)-ApostaInicial,2)
    porcentLucro = round((valorLucro/ApostaInicial*100),2)

    #print(porcentApostas)
    #print(valoresApostas)

    print(valorLucro,"R$")
    print(porcentLucro,"%")

else: 
    print("Não há uma surebet")
    

#print(somaIndice)
#print(len(indiceOdds))






