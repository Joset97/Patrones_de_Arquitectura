import cv2  # Necesita instalarse con `pip install opencv-python`
import pytesseract  # Necesita instalarse con `pip install pytesseract`
import numpy as np

class ImagePreprocessor:
    """Convierte la imagen en escala de grises y aplica binarización."""
    @staticmethod
    def process(image_path, blackboard):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, processed = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        blackboard.update("processed_image", processed)

class TextSegmenter:
    """Simula la segmentación de texto en caracteres individuales."""
    @staticmethod
    def segment(blackboard):
        processed_image = blackboard.get("processed_image")
        if processed_image is not None:
            segments = ["char1", "char2", "char3"]  # Simulación de segmentos
            blackboard.update("segments", segments)

class TextRecognizer:
    """Reconoce los caracteres en la imagen (simulación)."""
    @staticmethod
    def recognize(blackboard):
        segments = blackboard.get("segments")
        if segments:
            recognized_text = "ABC"  # Simulación de texto reconocido
            blackboard.update("recognized_text", recognized_text)
