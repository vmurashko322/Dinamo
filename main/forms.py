from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import AdvUser, Product


class ChangeAdvUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'messages')


class  UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Введите email')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Введите пароль',
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль',)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise ValidationError("Пароли должны совпадать")
        password_validation.validate_password(password1)
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields=('username','email','password1','password2','first_name','last_name','messages')
        # fields = ('username', 'email', 'password1', 'password2')


class CreateProductForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=4, required=True)
    price = forms.DecimalField(max_digits=4, decimal_places=1)


class CreateProductModel(forms.ModelForm):
    name = forms.CharField(max_length=50, min_length=4, required=True)
    price = forms.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        model = Product
        fields = '__all__'


# 13.04
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'