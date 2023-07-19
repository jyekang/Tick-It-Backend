from django.urls import path
from . import views

urlpatterns = [
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>', views.event_detail, name='event_detail')
]