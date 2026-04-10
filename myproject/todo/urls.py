from django.contrib import admin
from django.urls import path
from .views import todo,delete_task,update_task,edit_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",todo,name='todo'),
    path('delete/<int:id>/',delete_task, name='delete_task'),
    path('update/<int:id>/', update_task, name='update_task'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
]
