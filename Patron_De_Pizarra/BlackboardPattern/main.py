from blackboard import Blackboard
from control import Controller

if __name__ == "__main__":
    # Simula una imagen de entrada (cambia la ruta según tu imagen real)
    image_path = "imagen.jpg"  

    # Inicializa la pizarra y el controlador
    blackboard = Blackboard()
    controller = Controller(blackboard)

    # Ejecuta el sistema
    controller.run(image_path)
