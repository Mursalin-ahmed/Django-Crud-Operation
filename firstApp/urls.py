from django.urls import path

from .views import firstOne, delete_stu, update_stu

urlpatterns = [
    path('', firstOne, name = 'firstOne'),
    path('delete_stu/<int:id>/', delete_stu, name = 'delete_stu'),
    path('update_stu/<int:id>/', update_stu, name='update_stu'),
]
