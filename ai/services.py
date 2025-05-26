import cv2

def validar_tarefa_com_ia(before_path, after_path):
    try:
        img_before = cv2.imread(before_path)
        img_after = cv2.imread(after_path)

        if img_before is None or img_after is None:
            return False, "Erro ao carregar as imagens."

        # Ajuste de tamanho se necessário
        if img_before.shape != img_after.shape:
            img_after = cv2.resize(img_after, (img_before.shape[1], img_before.shape[0]))

        # Diferença absoluta
        diff = cv2.absdiff(img_before, img_after)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        non_zero = cv2.countNonZero(thresh)

        if non_zero > 5000:  # limiar ajustável
            return True, "Mudança detectada. Tarefa considerada realizada com sucesso."
        else:
            return False, "Diferença muito pequena. Tarefa não validada."
    except Exception as e:
        return False, f"Erro durante validação IA: {str(e)}"
