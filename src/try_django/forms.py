import email
from django import forms

class ContactForm(forms.Form):
    fill_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)