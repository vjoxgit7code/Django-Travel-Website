from.import views
from django.urls import path,include


urlpatterns = [

    path('',views.dj,name='dj'),

    #path('add/',views.home,name='home'),
]
