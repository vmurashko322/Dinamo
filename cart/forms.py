from django import forms
from .models import OrderDetail


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=zip(range(1, 21), range(1, 21)), coerce=int, label='Количество')


class OrderDetailForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = OrderDetail
        fields = '__all__'
