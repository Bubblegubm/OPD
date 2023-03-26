from .models import UserInfo, Friends
from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ["user", "user_name", "user_sec_name", "interests", "activity"]
        widgets = {
            "user": Select,
            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            "user_sec_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия пользователя'
            }),
            "interests": Select
        }


class FriendsInfoForm(ModelForm):
    class Meta:
        model = Friends
        fields = ["friends_name", "friends_sec_name", "friends_interests", "friends_activity"]
        widgets = {
            "friends_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            "friends_sec_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия пользователя'
            }),
            "friends_interests": Select,
            "friends_activity": Select
        }