from django.shortcuts import render, redirect, HttpResponse

from profiles.models import AddressDelivery
from profiles.services import create_user
from shop.models import Product
from profiles.forms import RegisterForm, LoginForm
from django.contrib.auth import logout, login, authenticate

def delivery(request):
    if request.method == 'GET':
        price = Product.objects.values('cost')
        return render(request, 'profiles/delivery_list.html', {'price': price})

def register(request):
    # if request.user.is_authenticated:
    #     return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            create_user(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password"],
            )
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "profiles/register.html", {"form": form})

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "profiles/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")