from django.contrib import admin
from django.urls import path, include

from . import views

from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
# Usando o quick start da documentação
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # Usando o quick start da documentação
    path('', include(router.urls)),

    path('get-user', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick),
    path('data/', views.user_manager),
]
