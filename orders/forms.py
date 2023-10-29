from django.contrib.auth.models import User
from django import forms
from .models import Orders


class OrderCreateForm(forms.ModelForm):
    class Meta:
        status_choices = (
            ("Pending", "Pending"),
            ("Delivered", "Delivered"),
            ("Cancelled", "Cancelled"),
        )
        priority_choices = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))
        model = Orders
        fields = ["customer", "product", "quantity", "status", "priority"]
        widgets = {
            "customer": forms.TextInput(attrs={"class": "form-control"}),
            "product": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "priority": forms.Select(
                choices=priority_choices, attrs={"class": "form-control"}
            ),
            "status": forms.Select(
                choices=status_choices, attrs={"class": "form-control"}
            ),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "readonly": True, "disabled": True}
            ),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
