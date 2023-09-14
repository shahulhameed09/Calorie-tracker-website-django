from django.contrib import admin
from .models import Food, Consume, Calories_Goal

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(Calories_Goal)
