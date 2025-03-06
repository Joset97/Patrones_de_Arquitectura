import subprocess
import json
import random

# Configuración
NUM_SLAVES = 4  # Número de procesos esclavos
TOTAL_NUMBERS = 1_000_000  # Cantidad total de números

# Generar una lista de números aleatorios
numbers = [random.randint(1, 100) for _ in range(TOTAL_NUMBERS)]

# Dividir la lista en partes iguales
chunk_size = TOTAL_NUMBERS // NUM_SLAVES
chunks = [numbers[i * chunk_size:(i + 1) * chunk_size] for i in range(NUM_SLAVES)]

# Lista para almacenar los resultados parciales
partial_sums = []

print("🔄 Iniciando procesos esclavos...")

# Ejecutar los esclavos en paralelo
for i, chunk in enumerate(chunks):
    print(f"📤 Enviando datos al esclavo {i + 1}...")

    process = subprocess.Popen(
        ["python3", "worker.py"],  # Si usas Windows, prueba con "python" en lugar de "python3"
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,  # Captura errores
        text=True
    )

    # Convertir los datos a formato JSON y enviarlos al esclavo
    json_data = json.dumps(chunk)
    output, error = process.communicate(json_data)  # Envía datos y espera respuesta

    if error:
        print(f"❌ Error en el esclavo {i + 1}: {error}")
    else:
        print(f"📥 Respuesta del esclavo {i + 1}: {output.strip()}")

    # Almacenar el resultado parcial
    partial_sums.append(int(output.strip()))

# Calcular la suma total
total_sum = sum(partial_sums)
print(f"✅ Suma total calculada: {total_sum}")
