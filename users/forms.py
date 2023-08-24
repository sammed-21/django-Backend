# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']  # Include relevant fields for user registration

  
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].required = True
#         self.fields['email'].required = True

from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ('username', 'email')