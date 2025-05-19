from django import forms
from .models import *
from django.contrib.auth.models import User


class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = "__all__"

class contectform(forms.ModelForm):
    class Meta:
        model = contect
        fields = "__all__"


class renthouseform(forms.ModelForm):
    class Meta:
        model = add_renthouse
        fields = "__all__"


class sellhouseform(forms.ModelForm):
    class Meta:
        model = add_sellhouse
        fields = "__all__"


class signupForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        
       
        
        # Check if the password is strong enough (e.g., length)
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return cleaned_data

    def save(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        
        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        return user

# Login form
class loginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

class AddSellHouseForm(forms.ModelForm):
    class Meta:
        model = add_sellhouse
        fields = ['name', 'address', 'price', 'description', 'image']


