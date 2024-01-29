""" Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
 """
km = float(input("Quantos km?"))

m = km * 1000
cm = km * 100000
mm = km * 1000000

print(f"A conversão de {km} km em m é {m} m.\n")
print(f"A conversão de {km} km em cm é {cm} cm.\n")
print(f"A conversão de {km} km em mm é {mm} mm.")
