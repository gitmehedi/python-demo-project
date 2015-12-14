from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '40'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
