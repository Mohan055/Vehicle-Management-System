import re
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Vehicle
from django.contrib.auth import authenticate

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    is_security_department = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'is_security_department']
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*]', password):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*).")
        return password

    def save(self, commit=True):
        # Save the User object
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        
        # Return the User instance instead of UserProfile
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")
        return cleaned_data
    
class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_name','vehicle_number','vehicle_type','delivery_challan_number','purchase_order_number','product','vehicle_image']
        


    