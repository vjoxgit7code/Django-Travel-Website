from.import views
from django.urls import path,include


urlpatterns = [

    path('register_form', views.register_form, name='register_form'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
