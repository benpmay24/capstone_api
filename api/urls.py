from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register("booking",views.BookingView)
router.register("menu",views.MenuView)

urlpatterns = [
    path('', views.index, name="home"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]