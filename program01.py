def contar_votos():
    
    votos = {1: 0, 2: 0, 3: 0, 4: 0}
    
    print("Ingrese los votos (1, 2, 3 o 4). Para finalizar, ingrese 0.")
    
    while True:
        voto = int(input("Ingrese un voto: "))
        
        if voto == 0:
            break
        elif voto in votos:
            votos[voto] += 1
        else:
            print("Voto no permitido. Por favor, ingrese un número entre 1 y 4.")
    
    # Calcular el total de votos
    total_votos = sum(votos.values())
    
    if total_votos == 0:
        print("No se han ingresado votos.")
    else:
        # Mostrar resultados
        print("\nResultados de la elección:")
        for candidato, cantidad in votos.items():
            porcentaje = (cantidad / total_votos) * 100
            print(f"Candidato {candidato}: {cantidad} votos ({porcentaje:.2f}%)")

# Ejecutar la función
contar_votos()
