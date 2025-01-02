from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminUserCreationForm

from accounts.models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = AdminUserCreationForm.Meta.fields + ('name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
