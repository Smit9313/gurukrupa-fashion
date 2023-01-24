from django.urls import path,include
from .views import my_view,MyModelViewSet    
from rest_framework import routers   

router = routers.DefaultRouter()
router.register(r'/mymodel', MyModelViewSet,basename='mymodel')

urlpatterns = [
        path('myview/',my_view,name='my_view'),
        path('',include(router.urls)),      
]
