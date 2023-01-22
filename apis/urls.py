from django.urls import path,include
from .views import my_view

urlpatterns = [
        path('myview/',my_view,name='my_view'),
]
