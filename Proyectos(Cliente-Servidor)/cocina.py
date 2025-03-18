import socket

def iniciar_servidor():
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enlazar el socket a una dirección y puerto
    direccion_servidor = ('localhost', 12345)
    print(f"Iniciando cocina en {direccion_servidor}")
    servidor_socket.bind(direccion_servidor)
    
    # Escuchar conexiones entrantes (hasta 5 clientes en espera)
    servidor_socket.listen(5)
    
    # Lista para almacenar los pedidos pendientes
    pedidos_pendientes = []
    
    while True:
        print("Esperando conexión de un mesero...")
        cliente_socket, direccion_cliente = servidor_socket.accept()
        print(f"Conexión establecida con {direccion_cliente}")
        
        try:
            while True:
                # Recibir datos del cliente (mesero)
                datos = cliente_socket.recv(1024)
                if not datos:
                    break
                
                # Procesar la solicitud (pedido)
                pedido = datos.decode('utf-8')
                print(f"Pedido recibido: {pedido}")
                
                # Agregar el pedido a la lista de pendientes
                pedidos_pendientes.append(pedido)
                
                # Enviar confirmación al cliente
                confirmacion = f"Pedido recibido: {pedido}. Total de pedidos pendientes: {len(pedidos_pendientes)}"
                cliente_socket.sendall(confirmacion.encode('utf-8'))
                print(f"Confirmación enviada a {direccion_cliente}")
        
        finally:
            # Cerrar la conexión con el cliente
            cliente_socket.close()
            print(f"Conexión con {direccion_cliente} cerrada.")

if __name__ == "__main__":
    iniciar_servidor()