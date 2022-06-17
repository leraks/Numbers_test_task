from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_static,),
    path('<int:page>/',views.view_static,),

]