from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = Profile
        fields = ['name', 'email']


