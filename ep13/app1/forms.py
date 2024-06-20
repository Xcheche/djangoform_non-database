from django import forms


from django import forms


class StudentInfo(forms.Form):
    name = forms.CharField(
        label="First Name",
        label_suffix="-",
        min_length=2,
        max_length=15,
        initial="Name",
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
        label="Email",
        initial="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "required": "required",
                "class": "form-control",
            },
        ),
    )
    message = forms.CharField(
        label="Your Message",
        initial="Message",
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
        label="Phone",
        initial="Phone",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter your phone number pls",
                "required": "required",
                "class": "form-control",
            }
        ),
    )

    # validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            raise forms.ValidationError(
                "Name should only contain alphabetic characters."
            )
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Add any custom validation for email if needed
        if "@" not in email:
            raise forms.ValidationError("Please  Enter a valid email")
        return email

    def clean_message(self):
        message = self.cleaned_data.get("message")
        # Add any custom validation for message if needed
        return message

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional cross-field validation here if needed
        return cleaned_data
