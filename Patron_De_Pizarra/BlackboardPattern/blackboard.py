class Blackboard:
    def __init__(self):
        self.data = {"image": None, "processed_image": None, "segments": None, "recognized_text": None}

    def update(self, key, value):
        """Actualiza un valor en la pizarra."""
        self.data[key] = value

    def get(self, key):
        """Obtiene un valor de la pizarra."""
        return self.data.get(key, None)

    def show(self):
        """Muestra el estado actual de la pizarra."""
        print("Estado de la pizarra:")
        for key, value in self.data.items():
            print(f"{key}: {value}")
