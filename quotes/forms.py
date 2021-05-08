from django import forms
from django.db.models.deletion import SET_DEFAULT
from .models import Quote
# class AddQuote(forms.Form):
#     name = forms.CharField(label='name', max_length=100)
#     email = forms.EmailField(label='email')
#     text = forms.CharField(label ='quote', max_length=500)
#     author = forms.CharField(label ='author',max_length=100)

class AddQuote(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'quote', 'author', 'email']