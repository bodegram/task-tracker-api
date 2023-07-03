from django.urls import path
from app import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('tasks', views.tasks, name="tasks"),
    path('tasks/<int:id>', views.task, name="task"),
    path('me', views.profile, name="me")
]