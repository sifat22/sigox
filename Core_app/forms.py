from django import forms
from django.forms import fields
from Core_app.models import Contact_Us


class Contact_Uss(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['message', 'name', 'title', 'email']

    def __init__(self, *args, **kwargs):
        super(Contact_Uss, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['placeholder'] = 'Enter message'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter  Name'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Subject'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
