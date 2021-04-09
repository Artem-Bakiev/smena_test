from django.conf.urls import url
from . import views

urlpatterns = [
    path('create_checks/', views.create_checks),
    path('new_checks/', views.new_checks),
    path('check/', views.get_check),
]