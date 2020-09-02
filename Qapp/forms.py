from django import forms
from .models import question,answer

class signin_form(forms.Form):
    name=forms.CharField(label="name",max_length=40)
    username=forms.CharField(label="username",max_length=40)
    password=forms.CharField(label="password",max_length=40)

class login_form(forms.Form):
    username=forms.CharField(label="username",max_length=40)
    password=forms.CharField(label="password",max_length=40)

class search_by_username(forms.Form):
    username=forms.CharField(label="search by username:",max_length=40)

class question_form(forms.ModelForm):
    class Meta:
        model=question
        fields=['Qtitle','Qdesc','img1','img2','img3','img4']