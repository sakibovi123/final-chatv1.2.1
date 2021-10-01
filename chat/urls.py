from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page, name='message'),
    path('all-contacts/', views.get_contact_page),
    path('selected-user/<str:username>/', views.get_or_create_thread, name="getuser"),
]
