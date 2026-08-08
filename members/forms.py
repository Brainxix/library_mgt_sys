from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "department",
            "registration_number",
            "date_joined",
            "status",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "member@example.com"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "department": forms.TextInput(attrs={"placeholder": "Department or class"}),
            "registration_number": forms.TextInput(attrs={"placeholder": "e.g. REG-001"}),
            "date_joined": forms.DateInput(attrs={"type": "date"}),
        }