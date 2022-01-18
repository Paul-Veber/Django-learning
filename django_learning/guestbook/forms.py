from django import forms

class GuestbookForm(forms.Form):
    pseudo = forms.CharField(label='Your name', max_length=200)
    body = forms.CharField(widget=forms.Textarea)
