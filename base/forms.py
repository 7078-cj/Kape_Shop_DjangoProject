from django.forms import ModelForm
from .models import Products,Orders , User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductCreationForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
class OrderCreationForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']