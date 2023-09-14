from django.forms import ModelForm
from myapp.models import Food, Calories_Goal
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class food_form(ModelForm):
    class Meta:
        model = Food
        fields = ['name','carbs','protein','fats','calories']
        
class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class calories_form(ModelForm):
    class Meta:
        model = Calories_Goal
        fields = ['Calories']