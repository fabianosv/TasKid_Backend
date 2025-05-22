# ai/utils.py
from PIL import Image, ImageChops

def validate_task_with_ai(image_path_before, image_path_after):
    """
    Compara duas imagens e retorna se houve mudança significativa.
    """
    try:
        before = Image.open(image_path_before)
        after = Image.open(image_path_after)

        diff = ImageChops.difference(before, after)
        bbox = diff.getbbox()

        if bbox:
            return True, "Diferenças detectadas na imagem."
        else:
            return False, "Nenhuma diferença detectada."

    except Exception as e:
        return False, f"Erro ao processar imagens: {str(e)}"
