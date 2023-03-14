from django.urls import path
from . import views

urlpatterns = [
    path('chat-free/', views.chatFree, name='chatFree')
]