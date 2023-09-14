from django.shortcuts import render, redirect
from .models import Food, Consume, Calories_Goal
from . forms import food_form, register, calories_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        if food_consumed == "--Select Food--":
            return redirect('/index')
        else:
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume)
            consume.save()
            foods = Food.objects.filter(user=request.user)

    else:
        foods = Food.objects.filter(user=request.user)
    consumed_food = Consume.objects.filter(user=request.user)
    calories = Calories_Goal.objects.filter(user= request.user)
    show = calories_form()

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food, 'calories':calories, 'show':show})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    consumed_food.delete()
    return redirect('/index')


def view_calories(request):
    kcal=Calories_Goal.objects.filter(user=request.user)
    formss = calories_form()
    if request.method=="POST":
        forms = calories_form(request.POST)
        if forms.is_valid():
            update=forms.save(commit=False)
            update.user=request.user
            update.save()
            return redirect('/index')
    return render(request, 'myapp/calories.html',{'kcal':kcal, 'formss':formss})


def add_food(request):
    food = food_form()
    if request.method=="POST":
        food = food_form(request.POST)
        if food.is_valid():
            update=food.save(commit=False)
            update.user=request.user
            update.save()
            return redirect('/view_food')
    return render(request, 'myapp/add_food.html', {'food':food})

def food(request):
    food = Food.objects.all()
    return render(request, 'myapp/food.html', {'food':food})

def delete_food(request, request_ID):
    food = Food.objects.get(id=request_ID)
    food.delete()
    return redirect('/view_food')

def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "invalid credentials")
            
    return render(request, 'myapp/logins.html')

def registers(request):
    form = register()
    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for '+user)
            return redirect('/logins')
        else:
            messages.error(request, form.errors.get('username'))
    context = {'form': form}
    return render(request, 'myapp/register.html',context)

def logouts(request):
    logout(request)
    return redirect('logins')

def home(request):
    return redirect('logins')

def edit_food(request, request_ID):
    food = Food.objects.get(id=request_ID)
    foods = food_form(request.POST or None, instance=food)
    if request.method=="POST":
        if foods.is_valid():
            foods.save()
            return redirect('/view_food')
    return render(request, 'myapp/edit_food.html', {'food':foods})


def update_kcal(request, request_ID):
    calories = Calories_Goal.objects.get(pk=request_ID)
    forms = calories_form(request.POST or None, instance=calories)
    if request.method=="POST":
        if forms.is_valid():
            forms.save()
            return redirect('/view_calories')
    return render(request, 'myapp/update_kcal.html', {'forms':forms})

def add_kcal(request):
    if request.method=="POST":
        form=calories_form(request.POST)
        if form.is_valid():
            up=form.save(commit=False)
            up.user=request.user
            up.save()
            return redirect('/index')