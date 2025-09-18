from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=email)

            # Verificamos la contraseña y que el usuario esté activo
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        except UserModel.DoesNotExist:
            return None

        except MultipleObjectsReturned:
            return UserModel.objects.filter(email=email).order_by("id").first()

        return None

    def user_can_authenticate(self, user):
        """
        Verifica que el usuario pueda autenticarse (está activo)
        """
        return user.is_active

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
            return user if self.user_can_authenticate(user) else None
        except UserModel.DoesNotExist:
            return None
