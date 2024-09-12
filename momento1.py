#Ejercicio 1..................................


def generar_serie():
    # Lista para almacenar los números de la serie
    serie = []
    
    # Primeros dos números de la serie
    a, b = 5, 8
    
    # Generar hasta obtener exactamente 100 números, excluyendo el 13
    while len(serie) < 100:
        if a != 13:  # Omitir el número 13
            serie.append(a)
        # Avanzar en la serie como Fibonacci
        a, b = b, a + b
    
    return serie

# Ejecutar el programa y mostrar los primeros 100 números
resultado = generar_serie()
print(resultado)







#Ejecicio 2...................................


import random

def calcular_salario_empleado(salario_base, porcentaje_comision, porcentaje_seguridad_social):
    # Calcular comisiones y deducción de seguridad social
    comision = salario_base * (porcentaje_comision / 100)
    deduccion_seguridad_social = salario_base * (porcentaje_seguridad_social / 100)
    
    # Calcular el salario neto
    salario_neto = salario_base + comision - deduccion_seguridad_social
    
    return salario_neto, comision, deduccion_seguridad_social

def generar_informacion_empleados(num_empleados):
    # Generar una lista de empleados con salarios base aleatorios
    empleados = []
    
    for i in range(num_empleados):
        salario_base = random.randint(1300000, 5000000)  # Salario base entre $1000 y $5000
        porcentaje_comision = random.uniform(5, 20)  # Comisión entre 5% y 20%
        porcentaje_seguridad_social = random.uniform(5, 10)  # Seguridad social entre 5% y 10%
        
        salario_neto, comision, deduccion_seguridad_social = calcular_salario_empleado(
            salario_base, porcentaje_comision, porcentaje_seguridad_social)
        
        # Almacenar la información del empleado en un diccionario
        empleado_info = {
            'ID': i + 1,
            'Salario Base': salario_base,
            'Comisión': round(comision, 2),
            'Deducción Seguridad Social': round(deduccion_seguridad_social, 2),
            'Salario Neto': round(salario_neto, 2)
        }
        
        empleados.append(empleado_info)
    
    return empleados

def imprimir_informacion_empleados(empleados):
    # Imprimir el listado de empleados con la información calculada
    print(f"{'ID':<5} {'Salario Base':<15} {'Comisión':<15} {'Deducción SS':<20} {'Salario Neto':<15}")
    print("-" * 70)
    
    for empleado in empleados:
        print(f"{empleado['ID']:<5} {empleado['Salario Base']:<15} {empleado['Comisión']:<15} {empleado['Deducción Seguridad Social']:<20} {empleado['Salario Neto']:<15}")

# Ejecutar el programa
num_empleados = 8
empleados = generar_informacion_empleados(num_empleados)
imprimir_informacion_empleados(empleados)





#Ejecicio 3...................................





def clasificar_numeros():
    # Listas para almacenar los números pares e impares
    pares = []
    impares = []
    
    # Solicitar 400 números al usuario
    for i in range(4):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        
        # Clasificar el número como par o impar
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    # Imprimir el listado de números
    print("\nListado de números pares e impares:")
    print(f"{'Número':<10} {'Clasificación':<15}")
    print("-" * 30)
    
    for numero in pares:
        print(f"{numero:<10} {'Par':<15}")
    
    for numero in impares:
        print(f"{numero:<10} {'Impar':<15}")
    
    # Imprimir el resumen del conteo
    print("\nResumen:")
    print(f"Total de números pares: {len(pares)}")
    print(f"Total de números impares: {len(impares)}")

# Ejecutar el programa
clasificar_numeros()






#Ejecicio 4...................................







def clasificar_leucemia(puntaje):
    # Determinar el nivel de leucemia basado en el puntaje
    if puntaje < 10:
        return "No tiene Leucemia"
    elif 11 <= puntaje <= 40:
        return "Nivel bajo de Leucemia"
    elif 41 <= puntaje <= 69:
        return "Nivel moderado de Leucemia"
    elif 70 <= puntaje <= 100:
        return "Nivel grave de Leucemia"
    else:
        return "Puntaje fuera del rango"

def procesar_pacientes(num_pacientes):
    # Listas para almacenar los resultados de clasificación
    resultados = []
    
    # Solicitar puntajes para los pacientes
    for i in range(num_pacientes):
        while True:
            try:
                puntaje = int(input(f"Ingrese el puntaje del paciente {i+1} (0-100): "))
                if 0 <= puntaje <= 100:
                    break
                else:
                    print("Puntaje inválido. Debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        
        # Clasificar el nivel de leucemia
        nivel = clasificar_leucemia(puntaje)
        
        # Almacenar el resultado
        resultados.append({
            'Paciente': i + 1,
            'Puntaje': puntaje,
            'Nivel de Leucemia': nivel
        })
    
    return resultados

def imprimir_resultados(resultados):
    # Imprimir el listado de pacientes y su nivel de leucemia
    print("\nListado de pacientes y su nivel de leucemia:")
    print(f"{'Paciente':<10} {'Puntaje':<10} {'Nivel de Leucemia':<30}")
    print("-" * 60)
    
    for resultado in resultados:
        print(f"{resultado['Paciente']:<10} {resultado['Puntaje']:<10} {resultado['Nivel de Leucemia']:<30}")

# Ejecutar el programa
num_pacientes = 4
resultados = procesar_pacientes(num_pacientes)
imprimir_resultados(resultados)





#Ejecicio 5...................................






def clasificar_funcionamiento(puntaje):
    # Determinar el estado de funcionamiento basado en el puntaje
    if puntaje == 2:
        return "Funcionamiento defectuoso"
    elif puntaje == 3:
        return "Funcionamiento moderado"
    elif puntaje == 4:
        return "Funcionamiento óptimo"
    else:
        return "Puntaje fuera del rango"

def procesar_cabinas(num_cabinas):
    # Lista para almacenar los resultados de clasificación
    resultados = []
    
    # Solicitar puntajes para las cabinas
    for i in range(num_cabinas):
        while True:
            try:
                puntaje = int(input(f"Ingrese el puntaje de la cabina {i+1} (2-4): "))
                if puntaje in [2, 3, 4]:
                    break
                else:
                    print("Puntaje inválido. Debe ser 2, 3, o 4.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        
        # Clasificar el funcionamiento
        estado = clasificar_funcionamiento(puntaje)
        
        # Almacenar el resultado
        resultados.append({
            'Cabina': i + 1,
            'Puntaje': puntaje,
            'Estado de Funcionamiento': estado
        })
    
    return resultados

def imprimir_resultados(resultados):
    # Imprimir el listado de cabinas y su estado de funcionamiento
    print("\nListado de cabinas y su estado de funcionamiento:")
    print(f"{'Cabina':<10} {'Puntaje':<10} {'Estado de Funcionamiento':<30}")
    print("-" * 60)
    
    for resultado in resultados:
        print(f"{resultado['Cabina']:<10} {resultado['Puntaje']:<10} {resultado['Estado de Funcionamiento']:<30}")

# Ejecutar el programa
num_cabinas = 4
resultados = procesar_cabinas(num_cabinas)
imprimir_resultados(resultados)

