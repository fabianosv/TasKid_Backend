# ai/validator.py
from .services import validar_tarefa_com_ia

def executar_validacao(before_image, after_image):
    return validar_tarefa_com_ia(before_image, after_image)
