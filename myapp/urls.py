from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.homepage),
    path('about/', views.about),
    path('contact/', views.contact),
    path('experiment/', views.experiment),
    path('experiment/<person>', views.experiment),
    path('experiment/<person>/greetings/<greet>', views.experiment_greet),
]