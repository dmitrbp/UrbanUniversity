from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль:', min_length=8, required=True)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль:', min_length=8, required=True)
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}), label='Введите свой возраст:', min_length=3, required=True)
    age = forms.IntegerField(min_value=18, label='Введите свой возраст:', required=True)
