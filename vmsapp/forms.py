
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Vehicle

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    is_security_department = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'is_security_department']

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
    
class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_name','vehicle_number','vehicle_type','delivery_challan_number','purchase_order_number','product','vehicle_image']
        


    