from datetime import date

from django import forms
from django.contrib.auth.models import User

from .models import Order


class OrderCreateForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Выберите имя",
        widget=forms.Select(attrs={"class": "form-control select mb-3"}),
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format="%d-%m-%Y %H:%M",
            attrs={"type": "datetime-local", "class": "form-control mb-3"},
        ),
        required=True,
        label="Выберите дату",
        initial=date.today().strftime("%d-%m-%Y %H:%M"),
    )

    class Meta:
        model = Order
        fields = ["name", "date"]
