from django import forms


class profile(forms.Form):
    image = forms.FileField()
    