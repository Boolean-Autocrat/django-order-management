from django.shortcuts import render, redirect, get_object_or_404
from .models import Orders
from .forms import OrderCreateForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect("dashboard")


def register_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        error = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if len(username) < 5:
            messages.error(request, "Username must be at least 5 characters long")
            error = True
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            error = True
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            error = True
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long")
            error = True
        if password.isdigit():
            messages.error(request, "Password must contain letters")
            error = True
        if password.isalpha():
            messages.error(request, "Password must contain numbers")
            error = True
        if password != password2:
            messages.error(request, "Passwords do not match")
            error = True
        if email.count("@") != 1 or email.count(".") < 1:
            messages.error(request, "Invalid email")
            error = True
        if error:
            return render(request, "auth/register.html", context)
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "auth/register.html", context)


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Invalid username or password")
            return render(request, "auth/login.html", context)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "auth/login.html", context)
    return render(request, "auth/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def profile_view(request):
    user_obj = User.objects.get(id=request.user.id)
    orders = Orders.objects.filter(vendor_id=request.user.id)
    context = {"profile": user_obj, "orders": orders}
    return render(request, "profile/profile.html", context)


@login_required(login_url="login")
def profile_edit(request):
    user_obj = get_object_or_404(User, id=request.user.id)
    profile_edit_form = ProfileEditForm(instance=user_obj)
    context = {"form": profile_edit_form}
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user_obj)
        if form.is_valid():
            user_obj.email = form.cleaned_data.get("email")
            user_obj.first_name = form.cleaned_data.get("first_name")
            user_obj.last_name = form.cleaned_data.get("last_name")
            user_obj.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            messages.error(request, form.errors)
            return render(request, "profile/edit.html", context)
    return render(request, "profile/edit.html", context)


def dashboard(request):
    context = {
        "orders": Orders.objects.all(),
        "orders_user": Orders.objects.filter(vendor_id=request.user.id),
        "user_id": request.user.id,
    }
    return render(request, "orders/dashboard.html", context)


@login_required(login_url="login")
def order_create(request):
    order_create_form = OrderCreateForm()
    context = {"form": order_create_form}
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        status_choices = ("Pending", "Delivered", "Cancelled")
        if form.data["status"] not in status_choices:
            messages.error(request, "Invalid status")
            return render(request, "orders/create.html", context)
        if form.is_valid():
            unsaved = form.save(commit=False)
            unsaved.vendor_id = request.user
            unsaved.save()
            return redirect("dashboard")
        else:
            messages.error(request, form.errors)
            return render(request, "orders/create.html", context)
    return render(request, "orders/create.html", context)


def order_details(request, order_id):
    context = {
        "order": Orders.objects.get(id=order_id),
        "order_id": order_id,
        "user_id": request.user.id,
    }
    return render(request, "orders/order.html", context)


@login_required(login_url="login")
def order_edit(request, order_id):
    if request.user.id != Orders.objects.get(id=order_id).vendor_id.id:
        messages.error(request, "You are not authorized to edit this order")
        return redirect("dashboard")
    data = get_object_or_404(Orders, id=order_id)
    order_edit_form = OrderCreateForm(instance=data)
    context = {
        "order": data,
        "order_id": order_id,
        "form": order_edit_form,
        "user_id": request.user.id,
    }
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        status_choices = ("Pending", "Delivered", "Cancelled")
        if form.data["status"] not in status_choices:
            messages.error(request, "Invalid status")
            return render(request, "orders/create.html", context)
        if form.is_valid():
            data.customer = form.cleaned_data.get("customer")
            data.product = form.cleaned_data.get("product")
            data.quantity = form.cleaned_data.get("quantity")
            data.status = form.cleaned_data.get("status")
            data.priority = form.cleaned_data.get("priority")
            data.save()
            messages.success(request, "Order updated successfully")
            return render(request, "orders/order.html", context)
    return render(request, "orders/edit.html", context)


@login_required(login_url="login")
def order_delete(request, order_id):
    if request.user.id != Orders.objects.get(id=order_id).vendor_id.id:
        messages.error(request, "You are not authorized to delete this order")
        return redirect("dashboard")
    context = {
        "order": Orders.objects.get(id=order_id),
        "order_id": order_id,
        "user_id": request.user.id,
    }
    if request.method == "POST":
        Orders.objects.get(id=order_id).delete()
        return redirect("dashboard")
    return render(request, "orders/delete.html", context)
