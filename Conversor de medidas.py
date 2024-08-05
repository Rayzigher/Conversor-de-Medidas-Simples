escolha = int(input("Digite o numero correspondente a medida que deseja converter: 1 = Km, 2 = Metros, 3 = Centimetros, 4 = Milimetros: "))
if escolha == 1:
    km = float(input("Digite quantos km deseja converter:"))
    conversor_km1 = km
    conversor_km2 = km * 1000
    conversor_km3 = km * 100000
    conversor_km4 = km * 1000000
    print(f"{conversor_km2} Metros, {conversor_km3} Cm, {conversor_km4} Milimetros. ")
elif escolha == 2:
    metros = float(input("Digite quantos metros deseja converter: "))
    conversor_m1 = metros / 1000
    conversor_m2 = metros
    conversor_m3 = metros * 100
    conversor_m4 = metros * 1000
    print(f"{conversor_m1} Quilometros,{conversor_m3} Cm, {conversor_m4} Milimetros. ")
elif escolha == 3:
    cm = float(input("Digite quantos centimetros deseja converter: "))
    conversor_cm1 = cm / 100000
    conversor_cm2 = cm / 100
    conversor_cm3 = cm
    conversor_cm4 = cm * 10
    print(f"{conversor_cm1} Quilometros, {conversor_cm2} Metros,{conversor_cm4} Milimetros. ")
elif escolha == 4:
    mili = float(input("Digite quantos milimetros deseja converter: "))
    conversor_mili1 = mili / 1000000
    conversor_mili2 = mili / 1000
    conversor_mili3 = mili / 10
    conversor_mili4 = mili
    print(f"{conversor_mili1} Quilometros, {conversor_mili2} Metros, {conversor_mili3} Cm. ")
else:
    print("Escolha invalida!")














#base
#digite_metro = float(input("Digite seu valor em METROS!"))
#centimetros = digite_metro * 100
#milimetros = digite_metro * 100
#print (f"Seu valor em centimetros é {centimetros} e em Milimetros é {milimetros}")



