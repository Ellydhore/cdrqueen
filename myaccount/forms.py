from django import forms
from usermanagement.models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'gender', 'date_of_birth', 'image']
