import cv2
import numpy as np
from django.core.files.storage import default_storage

def compare_images(image_path_before, image_path_after):
    try:
        before_img = cv2.imdecode(np.frombuffer(default_storage.open(image_path_before).read(), np.uint8), cv2.IMREAD_COLOR)
        after_img = cv2.imdecode(np.frombuffer(default_storage.open(image_path_after).read(), np.uint8), cv2.IMREAD_COLOR)

        if before_img is None or after_img is None:
            return False

        before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(before_gray, after_gray)
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        non_zero_count = np.count_nonzero(thresh)

        total_pixels = diff.size
        change_ratio = non_zero_count / total_pixels

        return change_ratio > 0.05  # Mínimo de 5% de mudança
    except Exception as e:
        print(f"[Erro IA] Falha na comparação de imagens: {e}")
        return False

