from django.urls import path
from .views import *

urlpatterns = [
    # blog urls
    path('', training_home_view, name='training-home'),
    path('course/<str:pk>/', course_details_view, name='course-details'),
    path('course/<str:pk>/', courses_view, name='courses'),
]

