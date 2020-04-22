from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path("d_course/<int:id>", views.d_course),
    path('delete/<int:id>', views.delete_course),
]