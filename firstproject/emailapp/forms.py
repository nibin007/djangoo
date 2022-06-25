from django import forms
class Filesup(forms.Form):
    file=forms.FileField()
    