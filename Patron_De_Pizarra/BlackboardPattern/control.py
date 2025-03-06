from knowledge_sources import ImagePreprocessor, TextSegmenter, TextRecognizer

class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run(self, image_path):
        """Ejecuta los módulos en orden."""
        print("\n📌 Iniciando procesamiento de imagen...\n")
        
        ImagePreprocessor.process(image_path, self.blackboard)
        self.blackboard.show()

        TextSegmenter.segment(self.blackboard)
        self.blackboard.show()

        TextRecognizer.recognize(self.blackboard)
        self.blackboard.show()

        print("\n✅ Proceso completado. Texto reconocido:", self.blackboard.get("recognized_text"))
