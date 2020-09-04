from django.urls import path
from . import views
                    
urlpatterns = [
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/<int:id>/destroy', views.destroy)
]