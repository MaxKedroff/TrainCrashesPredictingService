#здесь будет располагаться код модели YOLO
#на данный момент поставлена "болванка" для теста именно работы сервиса
import time
import random

class YOLOModel:
    def __init__(self):
        print("загрузка модели в память")
        self.model = None

    def predict(self, image_bytes):
        time.sleep(0.005)
        defect_detected = random.random() > 0.8

        details = {
            "defect_type": "scratch" if defect_detected else None,
            "confidence": round(random.uniform(0.7, 0.99), 2) if defect_detected else None,
            "coordinates": [random.randint(0, 100) for _ in range(4)] if defect_detected else None,
        }
        return {
            "defect_detected": defect_detected,
            "details": details
        }


model = YOLOModel()
def run_prediction(image_bytes):
    return model.predict(image_bytes)