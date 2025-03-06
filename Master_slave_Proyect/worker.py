import sys
import json

# Leer los datos desde stdin
input_data = sys.stdin.read()

# Deserializar los datos JSON
numbers = json.loads(input_data)

# Calcular la suma de los números recibidos
partial_sum = sum(numbers)

# Enviar la respuesta al maestro
print(partial_sum)
