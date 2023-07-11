
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class sigupform(UserCreationForm):
   
    class Meta:
        model=User
        fields=["first_name",'last_name','email','username','password1','password2']
        hdelp_texts={
            'username' : None,
            
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'input ', 'placeholder': 'Enter firstname'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter lastname'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control input', 'placeholder': 'Enter email'})
        self.fields['username'].widget = forms.EmailInput(attrs={'class': ' input', 'placeholder': 'Enter Username'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Confirm Password'})
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None





class signinform(forms.Form):
    username=forms.CharField(max_length=100,label='username',widget=forms.TextInput(attrs={'placeholder':'username','class':' input form-control form-control-lg'}))
    password=forms.CharField(max_length=100,label='password',widget=forms.PasswordInput(attrs={'placeholder':'password','class':' input form-control form-control-lg'}))
    
