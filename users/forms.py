from django.contrib.auth.forms import UserCreationForm

class customUserCredentionForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email']