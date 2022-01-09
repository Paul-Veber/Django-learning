from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=200)
