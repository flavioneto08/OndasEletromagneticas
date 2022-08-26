import math

op = 0
velo = float(3E8) #velocidade da luz
constMag = float(1.256E-06) #é a constante magnética mais conhecida como μ0

print("O programa a seguir foi desenvolvido pelos alunos: \n")
print("Flavio Eugenio de Oliveira Neto RA:22.221.027-0")
print("Arthur Soares Sousa RA:22.221.008-0\n")
print("O programa tem por finalidade de calcular as características de uma onda eletromagnética, basta o usuário escolher uma opção no menu, entrar com o valor daquela grandeza e nosso programa fará o resto\n")
print("As ondas eletromagnéticas são ondulações resultantes da interação entre campos elétricos e campos magnéticos, elas viajam na velocidade da luz e transportam energia. Ondas eletromagnéticas estão muito presentes em nosso dia a dia, alguns exemplos delas são o microondas, a luz que nós enxergamos, ondas de rádio, raio-x, entre diversas outras.\n")


while op != 8: #Menu de opções, será executado até o usuário digitar 8
  print('''[1] Frequência
[2] Comprimento de onda
[3] Número de onda
[4] Frequência angular
[5] Amplitude do campo elétrico
[6] Amplitude do campo magnético
[7] Intensidade
[8] Sair do programa''')
  op = int(input("\nCom qual grandeza você quer entrar o valor? "))
  print("---" * 20)
  if op == 1 :
    freq = float(input("\nEntre com a frequência (em Hz): "))
    #----Calculos----#
    compOnda = velo/freq
    numOnda = 2*math.pi/compOnda
    freqAng = 2*math.pi*freq
    #----Resultados----#
    print("\nComprimento de onda = " f'{compOnda:.3e}' " m")
    print("\nNúmero de onda = " f'{numOnda:.3e}' " rad/m")
    print("\nFrequência angular = " f'{freqAng:.3e}' " rad/s")
  
  elif op == 2 :
    compOnda = float(input("Entre com o comprimento da onda (em m): "))
    #----Calculos----#
    freq = velo/compOnda
    numOnda = 2*math.pi/compOnda
    freqAng = 2*math.pi*freq
    #----Resultados----#
    print("\nFrequência = " f'{freq:.3e}' " Hz")
    print("\nNúmero de onda = " f'{numOnda:.3e}' " rad/m")
    print("\nFrequência angular = " f'{freqAng:.3e}' " rad/s")
  
  elif op == 3 :
    numOnda = float(input("\nEntre com o número de onda (em rad/m): "))
    #----Calculos----#
    compOnda = 2*math.pi/numOnda
    freq = velo/compOnda
    freqAng = 2*math.pi*freq
    #----Resultados----#
    print("\nFrequência = " f'{freq:.3e}' " Hz")
    print("\nComprimento de onda = " f'{compOnda:.3e}' " m")
    print("\nFrequência angular = " f'{freqAng:.3e}' " rad/s")
    
  elif op == 4 :
    freqAng = float(input("\nEntre com a frequência angular (em rad/s): "))
    #----Calculos----#
    freq = freqAng/(2*math.pi)
    compOnda = velo/freq
    numOnda = 2*math.pi/compOnda
    #----Resultados----#
    print("\nComprimento de onda = " f'{compOnda:.3e}' " m")
    print("\nNúmero de onda = " f'{numOnda:.3e}' " rad/m")
    print("\nFrequência = " f'{freq:.3e}' " Hz")
    
  elif op == 5 :
    campEle = float(input("\nEntre com a amplitude do campo elétrico (em V/m): "))
    #----Calculos----#
    campMag = campEle/velo
    intensidade = (velo/(2*constMag))*campMag**2
    #----Resultados----#
    print("\nAmplitude do campo magnético = " f'{campMag:.3e}' " T")
    print("\nIntensidade = " f'{intensidade:.3e}' " W/m^2")
  
  elif op == 6 :
    campMag = float(input("\nEntre com a amplitude do campo magnético (em T): "))
    #----Calculos----#
    campEle = velo*campMag
    intensidade = (velo/(2*constMag))*campMag**2
    #----Resultados----#
    print("\nAmplitude do campo elétrico = " f'{campEle:.3e}' " V/m")
    print("\nIntensidade = " f'{intensidade:.3e}' " W/m^2")  
  
  elif op == 7 :
    intensidade = float(input("\nEntre com a intensidade (em W/m^2): "))
    #----Calculos----#
    campEle = math.sqrt((2*constMag*velo)*intensidade)
    campMag = campEle/velo
    #----Resultados----#
    print("\nAmplitude do campo elétrico = " f'{campEle:.3e}' " V/m")
    print("\nAmplitude do campo magnético = " f'{campMag:.3e}' " T")

  elif op<1 or op>8: #Se o usuario digitar algum número que não esta no menu dará erro
    print("\nOpção inválida!")
  print("---" * 20)  
print("\nPrograma encerrado!") #Caso o usuário digite 8 o programa encerrará
  