from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm): #상속
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','nickname','location','university']