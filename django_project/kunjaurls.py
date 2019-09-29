from django.urls import path

from . import kunja1

urlpatterns = [
    path('', kunja1.index, name='index'),
]