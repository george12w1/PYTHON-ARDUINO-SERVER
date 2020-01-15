from django import forms

class  ContactForm(forms.Form):
    pass
    descriere = forms.CharField()
    url = forms.CharField()