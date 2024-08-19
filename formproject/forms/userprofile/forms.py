from django import forms

class details(forms.Form):
    user_name = forms.CharField(label= "Enter the name")
    phone_number = forms.IntegerField(label= "Enter the phone number")
    email = forms.EmailField(label= "Enter the email")