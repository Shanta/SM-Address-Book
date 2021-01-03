from django.urls import path
from .views import HomePageView, AddressPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_address/', AddressPageView.as_view(), name='add_address'),
]
