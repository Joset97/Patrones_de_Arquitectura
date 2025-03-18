import socket

def enviar_pedido(plato, cantidad):
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectar el socket al servidor
    direccion_servidor = ('localhost', 12345)
    print(f"Conectando a la cocina en {direccion_servidor}")
    cliente_socket.connect(direccion_servidor)
    
    try:
        # Enviar el pedido al servidor
        pedido = f"{cantidad} x {plato}"
        mensaje = pedido.encode('utf-8')
        cliente_socket.sendall(mensaje)
        print(f"Pedido enviado: {pedido}")
        
        # Recibir la confirmación del servidor
        datos = cliente_socket.recv(1024)
        print(f"Confirmación recibida: {datos.decode('utf-8')}")
    
    finally:
        # Cerrar la conexión
        cliente_socket.close()

if __name__ == "__main__":
    plato = input("Introduce el nombre del plato: ")
    cantidad = input("Introduce la cantidad: ")
    enviar_pedido(plato, cantidad)