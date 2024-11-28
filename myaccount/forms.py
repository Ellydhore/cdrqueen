from django import forms
from usermanagement.models import CustomUser, Address

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'gender', 'date_of_birth', 'image']
        

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['phone_number', 'address_label', 'address_type', 'street', 'barangay', 'city', 'province', 'region', 'country', 'postal_code', 'specific_location']