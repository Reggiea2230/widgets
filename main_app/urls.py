from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('create/', views.CreateWidget, name='create_widget'),
    path('<int:widget_id>/delete/', views.DeleteWidget, name='delete_widget')
]