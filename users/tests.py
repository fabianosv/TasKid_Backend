from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class UserModelTest(TestCase):

    def test_create_user_parent(self):
        user = User.objects.create_user(
            username='parent_user',
            password='test1234',
            user_type='parent'
        )
        self.assertEqual(user.user_type, 'parent')
        self.assertEqual(str(user), "parent_user (Responsável)")

    def test_create_user_child(self):
        user = User.objects.create_user(
            username='child_user',
            password='test1234',
            user_type='child'
        )
        self.assertEqual(user.user_type, 'child')
        self.assertEqual(str(user), "child_user (Filho(a))")

    def test_invalid_user_type(self):
        # Testa que valores inválidos para user_type geram erro de validação
        user = User(
            username='invalid_user',
            user_type='invalid_type'
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # full_clean chama as validações do modelo
