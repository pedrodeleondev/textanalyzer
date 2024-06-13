frase=input("Ingresa una palabra: ")
a=input("Ingresa la primera letra: ")
b=input("Ingresa la segunda letra: ")
c=input("Ingresa la tercera letra: ")

print(f"La primera letra, la cual es {a}, aparece {frase.count(a)}.")
print(f"La segunda letra, la cual es {b}, aparece {frase.count(b)}.")
print(f"La tercera letra, la cual es {c}, aparece {frase.count(c)}.")

print(f"La frase tiene {len(frase.split())} frase.")

print(f"La primera letra es {frase[0]} y la última letra es {frase[len(frase)-1]}.")

print(f"Texto inverso: {frase[::-1]}")

print(f"¿Aparece la palabra?: {input('¿Qué palabra quieres verificar que esté en la frase?: ') in frase}")