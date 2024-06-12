from django import forms

from django import forms


class StudentInfo(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
                "required": "required",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "required": "required",
                "class": "form-control",
            }
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter your message",
                "required": "required",
                "class": "form-control",
            }
        ),
    )
    phone_no = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter your phone number",
                "required": "required",
                "class": "form-control",
            }
        ),
    )
