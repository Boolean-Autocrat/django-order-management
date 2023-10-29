from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("order/create/", views.order_create, name="order_create"),
    path("order/<str:order_id>/", views.order_details, name="order_details"),
    path("order/<str:order_id>/edit/", views.order_edit, name="order_edit"),
    path("order/<str:order_id>/delete/", views.order_delete, name="order_delete"),
]
