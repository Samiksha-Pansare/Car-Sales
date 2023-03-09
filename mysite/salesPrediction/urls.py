from django.urls import path, include
from . import views

urlpatterns = [
    path('/',views.home,name = "home"),
    path('/model',views.modelview,name="modelview")
]