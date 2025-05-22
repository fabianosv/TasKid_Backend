from django.test import TestCase
from .services import validar_tarefa_com_ia
from PIL import Image
import os

class ValidarTarefaComIATestCase(TestCase):
    def setUp(self):
        self.img_before = 'test_before.jpg'
        self.img_after = 'test_after.jpg'

        Image.new('RGB', (100, 100), color='white').save(self.img_before)
        Image.new('RGB', (100, 100), color='gray').save(self.img_after)

    def tearDown(self):
        if os.path.exists(self.img_before):
            os.remove(self.img_before)
        if os.path.exists(self.img_after):
            os.remove(self.img_after)

    def test_validar_tarefa_com_ia(self):
        resultado, mensagem = validar_tarefa_com_ia(self.img_before, self.img_after)
        self.assertIn(resultado, [True, False])
        self.assertIsInstance(mensagem, str)
        self.assertRegex(mensagem.lower(), r"diferenç|alteração|mudança")
