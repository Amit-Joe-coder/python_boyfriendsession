from django import forms

class my_form(forms.Form):
    bname=forms.CharField()
    age=forms.IntegerField()
    gname=forms.CharField()
