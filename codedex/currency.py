def konversi_fleksibel():
    
    PESOS_TO_USD = 0.058
    SOLES_TO_USD = 0.26
    REAIS_TO_USD = 0.20
    
    pesos = float(input("What do you have left in pesos? "))
    soles = float(input("What do you have left in soles? "))
    reais = float(input("What do you have left in reais? "))
    
    total = (pesos * PESOS_TO_USD + 
             soles * SOLES_TO_USD + 
             reais * REAIS_TO_USD)
    
    print(total)

konversi_fleksibel()