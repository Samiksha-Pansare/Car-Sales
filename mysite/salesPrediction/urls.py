from django.urls import path, include
from . import views

urlpatterns = [
    path('/',views.home,name = "home"),
    path('/model',views.modelview,name="modelview"),
    path('/addhistorydata', views.addhistorydata, name = "addhistorydata"),
    path('/addpredictions', views.addpredictions, name = "addpredictions"),
    path('/groupingdata', views.groupingdata, name = "groupingdata"),
    path('/forecast', views.forecast, name = "forecast"),
    path('/modelpage/<model>', views.modelpage, name = "modelpage"),
    path('/modelinsights/<model>', views.modelinsights, name = "modelinsights")
]