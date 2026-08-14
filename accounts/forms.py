from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from members.models import Member


User = get_user_model()


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "address",
            "profile_picture",
            "password1",
            "password2",
        ]

    def save(self, commit=True):

        user = super().save(commit=commit)

        if commit and user.role == "MEMBER":

            Member.objects.create(
                user=user,
                first_name=user.first_name or user.username,
                last_name="",
                email=user.email,
                phone_number=user.phone,
                department="Not specified",
                registration_number=f"MEM-{user.id}",
            )

        return user


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "phone",
            "address",
            "profile_picture",
        ]

        widgets = {
            "address": forms.Textarea(
                attrs={"rows": 3}
            ),
        }