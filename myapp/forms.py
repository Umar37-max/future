# forms.py
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    from_email = forms.EmailField(required=True, label='Your Email')
