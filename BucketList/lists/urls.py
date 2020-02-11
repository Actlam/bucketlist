from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from . import views
from rest_framework import routers
from .views import UserViewSet, EntryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
