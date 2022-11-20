from django import forms

from .models import crud_post, Post


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = crud_post
        fields = ['name', 'email', 'description', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'descriptionid'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    