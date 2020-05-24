from django.urls import path
from . import views

app_name = 'ToDoList'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('cross/<int:task_id>', views.cross, name='cross'),
    path('uncross/<int:task_id>', views.uncross, name='uncross'),
]
